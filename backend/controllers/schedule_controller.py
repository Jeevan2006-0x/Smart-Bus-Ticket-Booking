from flask import request, jsonify
from database.db import db
from models.schedule import Schedule


def add_schedule():
    data = request.get_json()

    schedule = Schedule(
        bus_id=data["bus_id"],
        route_id=data["route_id"],
        departure_time=data["departure_time"],
        arrival_time=data["arrival_time"],
        fare=data["fare"],
        available_seats=data["available_seats"]
    )

    db.session.add(schedule)
    db.session.commit()

    return jsonify({
        "message": "Schedule added successfully"
    }), 201