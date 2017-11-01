from flask import Blueprint, jsonify
import json
import requests
import pprint
from .config import dataUrl, dataHeaders

hasura_examples = Blueprint('hasura_examples', __name__)

@hasura_examples.route("/get_articles")
def articles():

    query = {
        'type': 'select',
        'args': {
            'table': 'article',
            'columns': [
                '*'
            ]
        }
    }
    print(json.dumps(query))
    print(dataUrl)

    response = requests.post( dataUrl, data = json.dumps(query), headers = dataHeaders)
    return jsonify(response.json())
