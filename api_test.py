#!/usr/bin/python3
# encoding: utf-8
import json

import requests

products = requests.get('http://127.0.0.1:5000/products')
print(json.dumps(products.json(), indent=4))

resp = requests.post(
    'http://127.0.0.1:5000/products',
    json={
        'name': 'Klawiatura',
        'category': 'Peryferia',
        'description': 'Opis klawiatury'
    }
)
print('Id nowego produktu: {}'.format(
    resp.json()['id']
))
