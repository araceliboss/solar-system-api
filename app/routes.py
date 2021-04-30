from app import db 
from app.models.planet import Planet 
from flask import request, Blueprint, make_response 

planets_bp = Blueprint("planets", __name__)
@planets_bp.route("/planets", methods=["GET"])
def get_planet():
    request_body = request.get_json()
    new_planet = Planet(title = request_body["title"], description = request_body["description"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.title} successfully created", 201)
