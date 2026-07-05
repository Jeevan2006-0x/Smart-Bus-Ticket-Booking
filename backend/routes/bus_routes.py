from flask import Blueprint

from controllers.bus_controller import (
    get_all_buses,
    get_bus,
    add_bus,
    update_bus,
    delete_bus
)

bus_bp = Blueprint("bus", __name__)

# Get All Buses
bus_bp.route("/buses", methods=["GET"])(get_all_buses)

# Get Bus By ID
bus_bp.route("/buses/<int:bus_id>", methods=["GET"])(get_bus)

# Add Bus
bus_bp.route("/buses", methods=["POST"])(add_bus)

# Update Bus
bus_bp.route("/buses/<int:bus_id>", methods=["PUT"])(update_bus)

# Delete Bus
bus_bp.route("/buses/<int:bus_id>", methods=["DELETE"])(delete_bus)