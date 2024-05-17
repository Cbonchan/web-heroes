from flask import Flask, request
from flask_cors import CORS

from time import sleep

from db.characters import get_all_characters, get_character_by_id, remove_character, add_character

app = Flask(__name__)
CORS(app)

@app.route("/characters")
def all_characters():
    return get_all_characters()

@app.route("/characters/<id>")
def character_by_id(id):
    sleep(1)
    return get_character_by_id(id)

@app.route("/characters/<id>",methods=["DELETE"])
def remove_character_by_id(id):
    return {"success": remove_character(id)}

@app.route("/characters", methods=["POST"])
def create_character():
    name= request.json.get("name")
    names= request.json.get("names")
    publisher= request.json.get("publisher")
    gender= request.json.get("gender")
    alingment= request.json.get("alingment")
    image= request.json.get("image")
    race= request.json.get("race")

    id = int(get_all_characters()[-1].get("id"))+1

    character= {
        "name": name,
        "names": names,
        "publisher": publisher,
        "gender": gender,
        "alingment": alingment,
        "image": image,
        "race": race,
        "id": id
    }
    return  { "success": add_character(character), "id" : id}
