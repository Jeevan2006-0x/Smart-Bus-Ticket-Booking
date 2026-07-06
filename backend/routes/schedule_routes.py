from flask import Blueprint
from controllers.schedule_controller import add_schedule

schedule_bp = Blueprint("schedule_bp", __name__)

schedule_bp.route("/schedule", methods=["POST"])(add_schedule)