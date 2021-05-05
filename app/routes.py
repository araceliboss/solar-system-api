from app import db 
from app.models.planet import Planet 
from flask import request, Blueprint, make_response 
from flask import jsonify

planets_bp = Blueprint("planets", __name__)

@planets_bp.route("/planets", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name = request_body["name"], description = request_body["description"])

    db.session.add(new_planet)
    db.session.commit()


    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("/planets", methods=["GET"])
def get_planet():
    planets = Planet.query.all()
    planets_response = []
    
    for planet in planets:
        planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description
            })
    return jsonify(planets_response)

def is_int(value):
    try: 
        return int(value)
    except ValueError:
        return False

@planets_bp.route("/planets/<planet_id>", methods=["GET", "PUT", "DELETE"])
def handle_planet(planet_id):
    planet = Planet.query.get(planet_id)
    
    if planet is None:
        return make_response("", 404)
    
    if not is_int(planet_id):
        return {
            "message": f"id {planet_id} must be an integer", 
            "success": False 
        }, 400

    if request.method == "GET":

        if planet:
            return planet.to_json(), 200


    elif request.method == "PUT":
        if planet: 
            form_data = request.get_json()
            planet.name = form_data["name"]
            planet.description = form_data["description"]
            db.session.commit()

            return make_response(f"Planet #{planet_id} successfully updated", 200)

    elif request.method == "DELETE":
        if planet:
            db.session.delete(planet)
            db.session.commit()

            return make_response(f"Planet #{planet_id} successfully deleted", 200)

    return make_response({
            "message": f"Planet with {planet_id} was not found", 
            "success": False 
        }, 404)