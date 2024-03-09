from flask import Flask, render_template, request

from dao import load_categories, load_products, get_product_by_id

app = Flask(__name__)


@app.route('/')
def hello_world():
    q = request.args.get("q")
    category_id = request.args.get("category_id")

    return render_template('index.html', categories=load_categories(), products=load_products(q, category_id))


@app.route('/products/<id>')
def details(id):
    product = get_product_by_id(id)
    return render_template('product-details.html', product=product)


if __name__ == '__main__':
    app.run(debug=True)
