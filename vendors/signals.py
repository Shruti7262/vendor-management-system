from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import PurchaseOrder
from django.db.models import  F, Avg

@receiver(post_save, sender=PurchaseOrder)
@receiver(post_delete, sender=PurchaseOrder)
def update_vendor_performance(sender, instance, **kwargs):
    vendor = instance.vendor
    update_on_time_delivery_rate(vendor)
    update_quality_rating_avg(vendor)
    update_average_response_time(vendor)
    update_fulfillment_rate(vendor)

def update_on_time_delivery_rate(vendor):
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
    on_time_orders = completed_orders.filter(delivery_date__lte=F('acknowledgment_date'))
    on_time_delivery_rate = (on_time_orders.count() / completed_orders.count()) * 100 if completed_orders.count() > 0 else 0
    vendor.on_time_delivery_rate = on_time_delivery_rate
    vendor.save()

def update_quality_rating_avg(vendor):
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed', quality_rating__isnull=False)
    quality_rating_avg = completed_orders.aggregate(avg_rating=Avg('quality_rating'))['avg_rating'] or 0
    vendor.quality_rating_avg = quality_rating_avg
    vendor.save()

def update_average_response_time(vendor):
    acknowledged_orders = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False)
    response_times = acknowledged_orders.annotate(response_time=F('acknowledgment_date') - F('issue_date'))
    average_response_time = response_times.aggregate(avg_response=Avg('response_time'))['avg_response'].total_seconds() if response_times else 0
    vendor.average_response_time = average_response_time
    vendor.save()

def update_fulfillment_rate(vendor):
    total_orders = PurchaseOrder.objects.filter(vendor=vendor)
    fulfilled_orders = total_orders.filter(status='completed')
    fulfillment_rate = (fulfilled_orders.count() / total_orders.count()) * 100 if total_orders.count() > 0 else 0
    vendor.fulfillment_rate = fulfillment_rate
    vendor.save()