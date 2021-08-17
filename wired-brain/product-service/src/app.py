from flask import Flask, jsonify, request
from db import db
from Product import Product

# products = [
#     {'id': 0, 'name': 'Product 0'},
#     {'id': 1, 'name': 'Product 1'}
# ]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@db/products'
db.init_app(app)

# curl -v http://localhost:5050/products
@app.route('/products', methods=['GET'])
def get_products():
    products = [product.json for product in Product.find_all()]
    return jsonify(products)


# curl -v http://localhost:5050/product/0
@app.route('/product/<int:id>', methods=['GET'])
def get_product_id(id):
    # product_list = [product for product in products if product['id'] == id]
    #     # if not product_list:
    #     #     return f'Product with id {id} not found!', 404
    product = Product.find_by_id(id)
    if product:
        return jsonify(product.json)
    return f'Product with id {id} not found!', 404


# curl
# --header "Content-Type: application/json"
# --request POST
# --data '{"name": "Product 3"}' -v http://localhost:5050/product/
@app.route('/product', methods=['POST'])
def add_product():
    # Retrieve the product from request body
    data = request.json

    # Generate an ID for the post
    # new_id = max([product['id'] for product in products]) + 1

    # Create a new product with id as 'None' since auto increment is set for ID column
    product = Product(None, data['name'])

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


# curl --header "Content-Type: application/json"
# --request PUT
# --data '{"name": "Updated Product 2"}'
# -v http://localhost:5050/product/<int:id>

@app.route('/product/<int:id>', methods=['PUT'])
def update_product(id):
    change_data = request.json

    # Find product if available
    # for product in products:
    #     if product['id'] == id:
    #         product['name'] = change_data['name']

    # Find if the ID exist. It's a class method and can be called directly
    existing_product = Product.find_by_id(id)
    if existing_product:
        existing_product.name = change_data["name"]
        existing_product.save_to_db()
        return jsonify(existing_product.json), 200
    return f'Product with id {id} not found', 404

# curl --request DELETE -v http://localhost:5050/product/2
@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    # for product in products:
    #     if product['id'] == id:
    #         products.remove(product)
    product_to_remove = Product.find_by_id(id)
    if product_to_remove:
        product_to_remove.delete_from_db()
        return jsonify(
            {
                'message': f'Product with id {id} removed'
            }), 200
    return f'Product with id {id} not found', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
    # app.run(host='0.0.0.0', debug=True)