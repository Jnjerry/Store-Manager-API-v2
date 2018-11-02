# Store-Manager-API

Store manager api is a flask api that helps storeowners to manage their products and sales with the help of store attendants

# STORE-MANAGER API
- Admin can add a product
- Admin/store attendant can get all products
- Admin/store attendant can get a specific product
- Store attendant can add a sale order
- Admin can get all sale order records
- Admin can delete a product
- Admin can update a product
## Available endpoints
| Http Method | Endpoint Route | Endpoint Functionality |
| --- | --- | --- |
| POST| /api/v2/auth/register | Signs Up User
| POST | /api/v2/auth/login | Log in User
| GET | /api/v2/products | retrieve all products
| GET |/api/v2/products/productid| retrieve a product by id
| GET| /api/v2/sales | retrieve all sales
| GET |/api/v2/products/saleid | retrieve a sale by id
| POST | /api/v2/products | create a product
| PUT | /api/v2/products/productid | update a product
| DELETE | /api/v2/products/productid | delete a product
| POST |  /api/v2/sales | create a sale


# API-DOCUMENTATION


## Prerequisites
- pip
- virtualenv
- python 3 or python 2.7

# How to Set Up locally
- Clone the repo<br>
git clone https://github.com/Jnjerry/Store-Manager-API-v2.git<br>
- create a virtual environment and activate it <br>
virtualenv env<br>
- install dependencies <br>
pip install -r requirements.txt<br>

# Running the tests
The tests have been written using the python module unittests.<br>
The tests can be run by using the following commands<br>
pytest -v

# Built with
Flask framework

# Author
Joan Ngugi
