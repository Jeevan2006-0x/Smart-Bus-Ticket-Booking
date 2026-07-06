from flask import Blueprint
from controllers.schedule_controller import add_schedule, get_schedules
from controllers.schedule_controller import (
    add_schedule,
    get_schedules,
    update_schedule
)
from controllers.schedule_controller import (
    add_schedule,
    get_schedules,
    update_schedule,
    delete_schedule
)

schedule_bp = Blueprint("schedule_bp", __name__)

schedule_bp.route("/schedule", methods=["POST"])(add_schedule)

schedule_bp.route("/schedules", methods=["GET"])(get_schedules)

schedule_bp.route("/schedule/<int:id>", methods=["PUT"])(update_schedule)

schedule_bp.route("/schedule/<int:id>", methods=["DELETE"])(delete_schedule)