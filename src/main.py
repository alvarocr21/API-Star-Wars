"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User,Characters,Planets,Favoritos

#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#Inicio Endpoints para user
@app.route('/user', methods=['GET'])
def get_users():

    # get all the user
    result = User.query.all()

    # map the results and your list of people  inside of the all_user variable
    all_user= list(map(lambda x: x.serialize(), result))

    return jsonify(all_user), 200

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        raise APIException('This user is not in the database', status_code=404)
    result = user.serialize()
    return jsonify(result), 200

  
@app.route('/user', methods=['POST'])
def add_user():
    request_body = request.get_json()
    user = User(fullName=request_body["fullName"],email=request_body["email"],password=request_body["password"],is_active=request_body["is_active"])
    db.session.add(user)
    db.session.commit()
   
    return jsonify({"Respuesta":"Los datos se almacenaron satisfactoriamente"}), 200


@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    
    user = User.query.get(user_id)
    if user is None:
        raise APIException('User not found', status_code=404)

    request_body = request.get_json()
    if "fullName" in request_body:
        user.fullName = request_body["fullName"]
    if "email" in request_body:
        user.email = request_body["email"]
    if "password" in request_body:
        user.password = request_body["password"]
    if "is_active" in request_body:
        user.is_active = request_body["is_active"]
    db.session.commit()
   
    return jsonify({"Respuesta":"Los datos se modificaron satisfactoriamente"}), 200

@app.route('/user/<int:user_id>', methods=['DELETE'])
def del_user(user_id):
    
    user = User.query.get(user_id)
    if user is None:
        raise APIException('User not found', status_code=404)

    db.session.delete(user)
    db.session.commit()
   
    return jsonify({"Respuesta":"Los datos se eliminaron satisfactoriamente"}), 200
#Final Endpoints para user  
  
#Inicio Endpoints  para characters

@app.route('/character', methods=['GET'])
def get_characters():

    # get all the user
    result = Characters.query.all()

    # map the results and your list of people  inside of the all_user variable
    all_characters= list(map(lambda x: x.serialize(), result))

    return jsonify(all_characters), 200

@app.route('/character/<int:character_id>', methods=['GET'])
def get_character(character_id):
  
    character = Characters.query.get(character_id)
    if character is None:
        raise APIException('This character is not in the database', status_code=404)
    result = character.serialize()
    return jsonify(result), 200


@app.route('/character', methods=['POST'])
def add_character():
    request_body = request.get_json()
    character = Characters(birth_year=request_body["birth_year"],eye_color=request_body["eye_color"],gender=request_body["gender"],hair_color=request_body["hair_color"],height=request_body["height"],mass=request_body["mass"],name=request_body["name"],photoUrl=request_body["photoUrl"],skin_color=request_body["skin_color"])
    db.session.add(character)
    db.session.commit()
   
    return jsonify({"Respuesta":"Los datos se almacenaron satisfactoriamente"}), 200

@app.route('/character/<int:character_id>', methods=['PUT'])
def update_character(character_id):
    
    character = Characters.query.get(character_id)
    if character is None:
        raise APIException('User not found', status_code=404)

    request_body = request.get_json()
    if "birth_year" in request_body:
        character.birth_year = request_body["birth_year"]
    if "eye_color" in request_body:
        character.eye_color = request_body["eye_color"]
    if "gender" in request_body:
        character.gender = request_body["gender"]
    if "hair_color" in request_body:
        character.hair_color = request_body["hair_color"]
    if "height" in request_body:
        character.height = request_body["height"]
    if "mass" in request_body:
        character.mass = request_body["mass"]
    if "name" in request_body:
        character.name = request_body["name"]
    if "photoUrl" in request_body:
        character.photoUrl = request_body["photoUrl"]
    if "skin_color" in request_body:
        character.skin_color = request_body["skin_color"]

    db.session.commit()
   
    return jsonify({"Respuesta":"Los datos se modificaron satisfactoriamente"}), 200

@app.route('/character/<int:character_id>', methods=['DELETE'])
def del_character(character_id):
    
    character = Characters.query.get(character_id)
    if character is None:
        raise APIException('User not found', status_code=404)

    db.session.delete(character)
    db.session.commit()
   
    return jsonify({"Respuesta":"Los datos se eliminaron satisfactoriamente"}), 200
#Final Endpoints  para characters

#Inicio Endpoints  para Planets

@app.route('/planet', methods=['GET'])
def get_planets():

    # get all the user
    result = Planets.query.all()

    # map the results and your list of people  inside of the all_user variable
    all_planets= list(map(lambda x: x.serialize(), result))

    return jsonify(all_planets), 200

@app.route('/planet/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):

    planet = Planets.query.get(character_id)
    if planet is None:
        raise APIException('This character is not in the database', status_code=404)
    result = planet.serialize()
    return jsonify(result), 200
 
@app.route('/planet', methods=['POST'])
def add_planet():
    request_body = request.get_json()
    planet = Planets(climate=request_body["climate"],galaxy=request_body["galaxy"],gravity=request_body["gravity"],name=request_body["name"],orbital_period=request_body["orbital_period"],photoUrl=request_body["photoUrl"],population=request_body["population"],surface_water=request_body["surface_water"],terrain=request_body["terrain"])
    db.session.add(planet)
    db.session.commit()
   
    return jsonify({"Respuesta":"Los datos se almacenaron satisfactoriamente"}), 200

@app.route('/planet/<int:planet_id>', methods=['PUT'])
def update_planet(planet_id):
    
    planet = Planets.query.get(planet_id)
    if planet is None:
        raise APIException('User not found', status_code=404)

    request_body = request.get_json()
    if "climate" in request_body:
        planet.climate = request_body["climate"]
    if "galaxy" in request_body:
        planet.galaxy = request_body["galaxy"]
    if "gravity" in request_body:
        planet.gravity = request_body["gravity"]
    if "name" in request_body:
        planet.name = request_body["name"]
    if "orbital_period" in request_body:
        planet.orbital_period = request_body["orbital_period"]
    if "photoUrl" in request_body:
        planet.photoUrl = request_body["photoUrl"]
    if "population" in request_body:
        planet.population = request_body["population"]
    if "surface_water" in request_body:
        planet.surface_water = request_body["surface_water"]
    if "terrain" in request_body:
        planet.terrain = request_body["terrain"]

    db.session.commit()
   
    return jsonify({"Respuesta":"Los datos se modificaron satisfactoriamente"}), 200

@app.route('/planet/<int:planet_id>', methods=['DELETE'])
def del_planet(planet_id):
    
    planet = Planets.query.get(planet_id)
    if planet is None:
        raise APIException('User not found', status_code=404)

    db.session.delete(planet)
    db.session.commit()
   
    return jsonify({"Respuesta":"Los datos se eliminaron satisfactoriamente"}), 200
#Final Endpoints  para Planets

#Inicio Endpoints  para Favoritos

#@app.route('/favorito', methods=['GET'])
#@app.route('/favorito/<int:character_id>', methods=['GET'])
@app.route('/favorito', methods=['POST'])
def add_favorito():
    request_body = request.get_json()
    favorito = Favoritos(user_id=request_body["user_id"],planets_id=request_body["planets_id"],characters_id=request_body["characters_id"])
    db.session.add(favorito)
    db.session.commit()
   
    return jsonify({"Respuesta":"Los datos se almacenaron satisfactoriamente"}), 200

#@app.route('/favorito/<int:favorito_id>', methods=['PUT'])

@app.route('/favorito/<int:favorito_id>', methods=['DELETE'])
def del_favorito(favorito_id):
    
    favorito = Favoritos.query.get(favorito_id)
    if favorito is None:
        raise APIException('User not found', status_code=404)

    db.session.delete(favorito)
    db.session.commit()
   
    return jsonify({"Respuesta":"Los datos se eliminaron satisfactoriamente"}), 200
#Final Endpoints  para Favoritos

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
