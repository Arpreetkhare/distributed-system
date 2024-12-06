Django API Assignment-
    This Django application provides API endpoints to create users, products, and orders. Each endpoint handles POST requests and interacts with the database using Django ORM.

Endpoints-
    Create User

        URL: api/create_user/
        Method: POST
        Description: Creates a new user by providing user_id, name, and email.

    Create Product

        URL: api/create_product/
        Method: POST
        Description: Creates a new product by providing product_id, name, and price.

    Create Order

        URL: api/create_order/
        Method: POST
        Description: Creates a new order by providing order_id, user_id, product_id, and quantity.

clone Repo :

    ```bash
        https://github.com/Arpreetkhare/distributed-system.git
        
Requirements
    Python 3.x
    Django
    SQLite (default database)
    How to Run
Install dependencies:

    bash
        pip install -r requirements.txt
Run migrations:

    bash
        python manage.py migrate
Start the development server:

    bash
        python manage.py runserver
