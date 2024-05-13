from flask import Flask
from db.characters import get_all_characters
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "hola"
    
@app.route("/characters")
def characters():
    return get_all_characters()
   