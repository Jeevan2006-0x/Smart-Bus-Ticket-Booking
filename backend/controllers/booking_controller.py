from flask import request, jsonify
from database.db import db
from models.booking import Booking


def add_booking():
    data = request.get_json()

    booking = Booking(
        user_id=data["user_id"],
        schedule_id=data["schedule_id"],
        seat_number=data["seat_number"]
    )

    db.session.add(booking)
    db.session.commit()

    return jsonify({
        "message": "Booking created successfully"
    }), 201

def get_bookings():
    bookings = Booking.query.all()

    result = []

    for booking in bookings:
        result.append({
            "id": booking.id,
            "user_id": booking.user_id,
            "schedule_id": booking.schedule_id,
            "seat_number": booking.seat_number,
            "booking_status": booking.booking_status,
            "created_at": str(booking.created_at)
        })

    return jsonify(result), 200