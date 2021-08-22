from flask import Flask, jsonify, request
from db import db
from Product import Product
import logging.config
from sqlalchemy import exc
import configparser

# products = [
#     {'id': 0, 'name': 'Product 0'},
#     {'id': 1, 'name': 'Product 1'}
# ]

# Configure the logging package from the logging ini file
logging.config.fileConfig("/config/logging.ini", disable_existing_loggers=False)

# Get a logger for our module
log = logging.getLogger(__name__)


def get_database_url():
    # Load our database configuration
    config = configparser.ConfigParser()
    config.read('/config/db.ini')
    database_configuration = config['mysql']
    host = database_configuration['host']
    username = database_configuration['username']
    db_password = open('/run/secrets/db_password')
    password = db_password.read()
    database = database_configuration['database']
    database_url = f'mysql://{username}:{password}@{host}/{database}'
    log.info(f'Connecting to database: {database_url}')
    return database_url


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = get_database_url()
db.init_app(app)


# curl -v http://localhost:5050/products
@app.route('/products', methods=['GET'])
def get_products():
    log.debug('GET /products')
    try:
        products = [product.json for product in Product.find_all()]
        return jsonify(products)
    except exc.SQLAlchemyError:
        log.exception('An exception occurred while retrieving all products.')
        return 'An exception occurred while retrieving all products', 500


# curl -v http://localhost:5050/product/0
@app.route('/product/<int:id>', methods=['GET'])
def get_product_id(id):
    log.debug(f'GET /product/{id}')
    # product_list = [product for product in products if product['id'] == id]
    #     # if not product_list:
    #     #     return f'Product with id {id} not found!', 404
    try:
        product = Product.find_by_id(id)
        if product:
            return jsonify(product.json)
        log.warning(f'GET /product/{id}: Product not found')
        return f'Product with id {id} not found!', 404
    except exc.SQLAlchemyError:
        log.exception(f'An exception occurred while retrieving product {id}')
        return f'An exception occurred while retrieving product {id}', 500


# curl
# --header "Content-Type: application/json"
# --request POST
# --data '{"name": "Product 3"}' -v http://localhost:5050/product/
@app.route('/product', methods=['POST'])
def add_product():
    # Retrieve the product from request body
    data = request.json
    log.debug(f'POST /product with product: {data}')

    # Generate an ID for the post
    # new_id = max([product['id'] for product in products]) + 1

    # Create a new product with id as 'None' since auto increment is set for ID column
    product = Product(None, data['name'])

    try:
        # Save the Product to the database
        product.save_to_db()

        # Create new product
        # new_product = {
        #     'id': new_id,
        #     'name': data['name']
        # }
        # add new product to the array
        # products.append(new_product)

        return jsonify(product.json), 201
    except exc.SQLAlchemyError:
        log.exception(f'An exception occurred while creating product with name: {product.name}')
        return f'An exception occurred while creating product with name: {product.name}', 500


# curl --header "Content-Type: application/json"
# --request PUT
# --data '{"name": "Updated Product 2"}'
# -v http://localhost:5050/product/<int:id>

@app.route('/product/<int:id>', methods=['PUT'])
def update_product(id):
    change_data = request.json
    logging.debug(f'PUT /product/{id}')
    # Find product if available
    # for product in products:
    #     if product['id'] == id:
    #         product['name'] = change_data['name']

    # Find if the ID exist. It's a class method and can be called directly
    try:
        existing_product = Product.find_by_id(id)
        if existing_product:
            existing_product.name = change_data["name"]
            existing_product.save_to_db()
            return jsonify(existing_product.json), 200
        log.warning(f'PUT /product/{id} : Existing product not found')
        return f'Product with id {id} not found', 404
    except exc.SQLAlchemyError:
        log.exception(f'An exception occurred while creating product with name: {change_data.name}')
        return f'An exception occurred while creating product with name: {change_data.name}', 500


# curl --request DELETE -v http://localhost:5050/product/2
@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    log.debug(f'DELETE /product/{id}')
    # for product in products:
    #     if product['id'] == id:
    #         products.remove(product)
    try:
        product_to_remove = Product.find_by_id(id)
        if product_to_remove:
            product_to_remove.delete_from_db()
            return jsonify(
                {
                    'message': f'Product with id {id} removed'
                }), 200
        log.warning(f'DELETE /product/{id}: Existing product not found')
        return f'Product with id {id} not found', 404
    except exc.SQLAlchemyError:
        log.exception(f'An exception occured while deleting the product with id: {id}')
        return f'An exception occurred while deleting the product with id: {id}', 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
    # app.run(host='0.0.0.0', debug=True)
