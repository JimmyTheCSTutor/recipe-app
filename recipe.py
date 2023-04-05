from flask import Flask, render_template
import json

app = Flask(__name__)

with open('recipe_data.json', 'r') as recipes:
    recipe_dict = json.load(recipes)   

# TODO: Implement the three routes as described in the description.


# TODO: import and register the api blueprint from api.py


if __name__ == '__main__':
    app.run(port=8000, debug=True)
