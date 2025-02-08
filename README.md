# vendor-management-system
## Overview
The Vendor Management System is a Django-based application that allows you to manage vendors, track purchase orders, and evaluate vendor performance metrics. It provides RESTful APIs for creating, updating, and retrieving vendor and purchase order data, as well as calculating and storing vendor performance metrics.


## Features
1. Vendor Management:

    * Create, update, retrieve, and delete vendor profiles.
    
    * Store vendor details such as name, contact information, address, and a unique vendor code.

2. Purchase Order Tracking:

    * Create, update, retrieve, and delete purchase orders.
    
    * Track purchase order details such as PO number, vendor, order date, delivery date, items, quantity, and status.

3. Vendor Performance Evaluation:

    * Automatically calculate and store performance metrics for vendors:
    
    * On-Time Delivery Rate: Percentage of orders delivered on or before the promised date.
    
    * Quality Rating Average: Average quality rating of completed purchase orders.
    
    * Average Response Time: Average time taken by the vendor to acknowledge purchase orders.
    
    * Fulfillment Rate: Percentage of purchase orders fulfilled without issues.
    
    * Historical performance records are stored for trend analysis.

4. RESTful APIs:

   * Built using Django REST Framework (DRF).
  
   * Token-based authentication for secure access.


# Setup Instructions
## Prerequisites
 * Python 3.8+
 * Django 4.0+
 * Django REST Framework
 * SqlLite3 (or any other database supported by Django)


## Installation

1. Clone the repository:
   * git clone [https://github.com/your-username/vendor-management-system.git](https://github.com/Shruti7262/vendor-management-system)
   * cd vendor-management-system
2. Create a virtual environment:
   > you can use any virtual environment you like. Here I am using pipenv
   * pip install pipenv  
   * pipenv install 
   * pipenv shell
4. Install dependencies:
   * pipenv install -r requirements.txt
5. Set up the database:
   * python manage.py makemigrations
   * python manage.py migrate
6. Create a superuser:
   * python manage.py createsuperuser
7. Run the development server:
   * python manage.py runserver
8. Access the API:
   * http://127.0.0.1:8000/api/
