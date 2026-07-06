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

from models.schedule import Schedule


def get_schedules():
    schedules = Schedule.query.all()

    result = []

    for schedule in schedules:
        result.append({
            "id": schedule.id,
            "bus_id": schedule.bus_id,
            "route_id": schedule.route_id,
            "departure_time": str(schedule.departure_time),
            "arrival_time": str(schedule.arrival_time),
            "fare": schedule.fare,
            "available_seats": schedule.available_seats
        })

    return jsonify(result), 200

def update_schedule(id):
    data = request.get_json()

    schedule = Schedule.query.get(id)

    if not schedule:
        return jsonify({"message": "Schedule not found"}), 404

    schedule.bus_id = data["bus_id"]
    schedule.route_id = data["route_id"]
    schedule.departure_time = data["departure_time"]
    schedule.arrival_time = data["arrival_time"]
    schedule.fare = data["fare"]
    schedule.available_seats = data["available_seats"]

    db.session.commit()

    return jsonify({
        "message": "Schedule updated successfully"
    }), 200

def delete_schedule(id):
    schedule = Schedule.query.get(id)

    if not schedule:
        return jsonify({"message": "Schedule not found"}), 404

    db.session.delete(schedule)
    db.session.commit()

    return jsonify({
        "message": "Schedule deleted successfully"
    }), 200