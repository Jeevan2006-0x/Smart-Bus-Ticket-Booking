from flask import Blueprint
from controllers.bus_controller import add_bus, get_buses

bus_bp = Blueprint("bus", __name__)

bus_bp.route("/bus", methods=["POST"])(add_bus)
bus_bp.route("/buses", methods=["GET"])(get_buses)