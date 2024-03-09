import json

from flask import request


def load_categories():
    with open('data/categories.json', encoding='utf-8') as f:
        return json.load(f)


def load_products(q=None, category_id=None):
    with open('data/products.json', encoding='utf-8') as f:
        products = json.load(f)

        if q:
            products = [p for p in products if p['name'].find(q) >= 0]

        if category_id:
            products = [p for p in products if p['category_id'].__eq__(int(category_id))]

        return products


def get_product_by_id(product_id):
    with open('data/products.json', encoding='utf-8') as f:
        products = json.load(f)

        for p in products:
            if p['id'].__eq__(int(product_id)):
                return p
