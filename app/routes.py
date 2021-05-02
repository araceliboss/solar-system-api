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
                "title": planet.name,
                "description": planet.description
            })
    return jsonify(planets_response)


@planets_bp.route("/<planet_id>", methods=["GET"])
def one_planet(planet_id):
    planet = Planet.query.get(planet_id)
    return {
            "id": planet.id,
            "title": planet.name,
            "description": planet.description
    }
