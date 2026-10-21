from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

a = "Daniel"

page_not_found_text = "Esta página NÃO existe pequiníssimo criolo."

piadas = [{
    "id": 1,
    "content": "Quanto é que é 1 + 1? Eu não sei, é por isso que estou a perguntar.",
    "autor": a
},
{
    "id": 2,
    "content": "Porque é que EU atravessei a estrada? Porque eu quis, I guess.",
    "autor": a
},
{
    "id": 3,
    "content": "Hey. It's just that, hey!",
    "autor": a
},
{
    "id": 4,
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam malesuada mattis est. In eget luctus dolor. Aliquam eleifend consequat turpis. Cras fringilla dignissim mauris, semper cursus elit consequat a. Pellentesque maximus lobortis massa sit amet convallis. Proin neque ante, posuere ac magna in, elementum luctus neque. In sollicitudin fringilla justo, vel dignissim justo ullamcorper non. Donec ullamcorper pharetra ex ac auctor. Mauris ultricies tempor ipsum, a sagittis dui ullamcorper vitae. Proin eu rutrum dui. Aenean ornare blandit nisi ac ultricies. Cras eleifend, leo et tincidunt malesuada, ligula augue tristique urna, sit amet congue felis enim vel nibh. Mauris sed nulla vel lectus sodales interdum vel eget purus. Donec vitae odio neque. Maecenas molestie id metus id cursus. Pellentesque sed augue et arcu consectetur pellentesque et id lorem.",
    "autor": a
}]

brainrots = [{
    "id": 1,
    "content": "Tuff tuff tuff sahur",
    "autor": a
},
{
    "id": 2,
    "content": "Those who eat mangos",
    "autor": a
},
{
    "id": 3,
    "content": "Me after imagining 220 8k apples rotating in 200 fps with 1000 iq *skull emoji*",
    "autor": a
}]

@app.route("/")
def index():
    return 'Entra na página de piadas.'

@app.route("/piada")
def piada():
    return jsonify(random.choice(piadas)["content"])

@app.route("/piada/<int:id>", methods=['GET'])
def piada_especifica(id):
    if id < 1 or id > len(piadas):
        return page_not_found_text
    return jsonify(piadas[id - 1]["content"])

@app.route("/brainrot")
def brainrot():
    return jsonify(random.choice(brainrots)["content"])

@app.route("/brainrot/<int:id>", methods=['GET'])
def brainrot_especifico(id):
    if id < 1 or id > len(brainrots):
        return page_not_found_text
    return jsonify(brainrots[id - 1]["content"])

app.run(host="0.0.0.0", port=8081)