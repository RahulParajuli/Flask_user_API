from flask import Flask
from flask_bcrypt import Bcrypt
from flask_mongoengine import MongoEngine
from flask_cors import CORS
import certifi
# from user import routes

app = Flask(__name__)
CORS(app)

app.config['MONGODB_SETTINGS'] = {
    "db": "user",
    "host": "mongodb://localhost:27017",
    "port": 27017,
    "tlsCAFile": certifi.where()
}

db = MongoEngine()
db.init_app(app)

Bcrypt = Bcrypt(app)


