from flask import Blueprint, jsonify, request
import json

api_blueprint = Blueprint('api', __name__, url_prefix='/api')
with open('recipe_data.json', 'r') as recipes:
    recipe_dict = json.load(recipes)

# TODO: add the search api endpoint to return a list of recipes matching the keyword.
