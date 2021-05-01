from app import db 
from app.models.planet import Planet 
from flask import request, Blueprint, make_response 

planets_bp = Blueprint("planets", __name__)

@planets_bp.route("/planets", methods=["POST"])
def get_planet():
    request_body = request.get_json()
    new_planet = Planet(name = request_body["name"], description = request_body["description"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)
