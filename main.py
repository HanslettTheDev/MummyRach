from flask import Flask
from flask_cors import CORS

# instantiate app
app = Flask(__name__)
app.config.from_object(__name__)

# enable cors
CORS(app, resources={r'/*': {'origins': '*'}})