from flask import Blueprint, render_template, request, flash, jsonify
import redis
import json

# Se establese la conexión de redis en la base de datos 0
# redis://localhost:6379
collection = redis.Redis(host='localhost', port=6379, db=0)
hashName = "diccionario"


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():     
   
    list = collection.hgetall(hashName)
    return render_template("home.html", palabras = list)


@views.route('/eliminar-palabra', methods=['POST'])
def delete_note():
    model = json.loads(request.data)
    palabra = model['palabra']   

    collection.hdel(hashName, palabra)

    return jsonify({})

@views.route('/editar', methods=['GET'])
def editar():    
    palabra = request.args.get('palabra')
    significado = collection.hget(hashName, palabra)
    
    model = {"palabra" : palabra, "significado" : significado.decode()}
    return render_template("editar.html", model = model)

@views.route('/ver-palabra', methods=['GET'])
def ver_palabra():    
    palabra = request.args.get('palabra')
    significado = collection.hget(hashName, palabra)
    
    model = {"palabra" : palabra, "significado" : significado.decode()}

    return render_template("ver.html", model = model)

@views.route('/agregar', methods=['GET'])
def agregar():    
    return render_template("agregar.html")

@views.route('/agregarPalabra', methods=['POST'])
def agregar_palabra():
    palabra = request.form.get('palabra')
    significado = request.form.get('significado')
    collection.hset(hashName, palabra, significado)

   

    list = collection.hgetall(hashName)

    return render_template("home.html", palabras = list)
