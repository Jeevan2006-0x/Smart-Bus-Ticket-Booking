from flask import Blueprint
from controllers.route_controller import add_route, get_routes

route_bp = Blueprint("route_bp", __name__)

route_bp.route("/route", methods=["POST"])(add_route)

route_bp.route("/routes", methods=["GET"])(get_routes)