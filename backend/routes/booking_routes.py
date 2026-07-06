from flask import Blueprint
from controllers.booking_controller import add_booking
from controllers.booking_controller import (
    add_booking,
    get_bookings
)
from controllers.booking_controller import (
    add_booking,
    get_bookings,
    update_booking
)
from controllers.booking_controller import (
    add_booking,
    get_bookings,
    update_booking,
    delete_booking
)

booking_bp = Blueprint("booking_bp", __name__)

booking_bp.route("/booking", methods=["POST"])(add_booking)

booking_bp.route("/bookings", methods=["GET"])(get_bookings)

booking_bp.route("/booking/<int:id>", methods=["PUT"])(update_booking)

booking_bp.route("/booking/<int:id>", methods=["DELETE"])(delete_booking)