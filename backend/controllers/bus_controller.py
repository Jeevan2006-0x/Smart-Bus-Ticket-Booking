from flask import request, jsonify
from database.db import db
from models.bus import Bus


def add_bus():
    data = request.get_json()

    bus_number = data.get("bus_number")
    bus_name = data.get("bus_name")
    bus_type = data.get("bus_type")
    total_seats = data.get("total_seats")

    # Check if bus number already exists
    existing_bus = Bus.query.filter_by(bus_number=bus_number).first()

    if existing_bus:
        return jsonify({
            "message": "Bus already exists"
        }), 400

    bus = Bus(
        bus_number=bus_number,
        bus_name=bus_name,
        bus_type=bus_type,
        total_seats=total_seats
    )

    db.session.add(bus)
    db.session.commit()

    return jsonify({
        "message": "Bus Added Successfully"
    }), 201
def get_buses():

    buses = Bus.query.all()

    data = []

    for bus in buses:
        data.append({
            "id": bus.id,
            "bus_number": bus.bus_number,
            "bus_name": bus.bus_name,
            "bus_type": bus.bus_type,
            "total_seats": bus.total_seats
        })

    return jsonify(data), 200