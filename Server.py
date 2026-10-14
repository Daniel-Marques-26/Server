from flask import Flask
import random

app = Flask(__name__)

piadas = ["Quanto é que é 1 + 1? Eu não sei, é por isso que estou a perguntar.",
          "Porque é que EU atravessei a estrada? Porque eu quis, I guess.",
          "Hey. It's just that, hey!",
          "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam malesuada mattis est. In eget luctus dolor. Aliquam eleifend consequat turpis. Cras fringilla dignissim mauris, semper cursus elit consequat a. Pellentesque maximus lobortis massa sit amet convallis. Proin neque ante, posuere ac magna in, elementum luctus neque. In sollicitudin fringilla justo, vel dignissim justo ullamcorper non. Donec ullamcorper pharetra ex ac auctor. Mauris ultricies tempor ipsum, a sagittis dui ullamcorper vitae. Proin eu rutrum dui. Aenean ornare blandit nisi ac ultricies. Cras eleifend, leo et tincidunt malesuada, ligula augue tristique urna, sit amet congue felis enim vel nibh. Mauris sed nulla vel lectus sodales interdum vel eget purus. Donec vitae odio neque. Maecenas molestie id metus id cursus. Pellentesque sed augue et arcu consectetur pellentesque et id lorem."]

@app.route("/")
def index():
    return 'Entra na página de piadas.'

@app.route("/piada")
def piada():
    return random.choice(piadas)

@app.route("/piada/<int:id>", methods=['GET'])
def piada_especifica(id):
    if id < 1 or id > len(piadas):
        return "Esta página NÃO existe pequiníssimo criolo."
    return piadas[id - 1]

app.run(host="0.0.0.0", port=8080)