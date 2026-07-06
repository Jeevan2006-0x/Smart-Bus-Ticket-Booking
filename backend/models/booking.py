from database.db import db

class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, nullable=False)

    schedule_id = db.Column(db.Integer, nullable=False)

    seat_number = db.Column(db.String(10), nullable=False)

    booking_status = db.Column(
        db.String(20),
        default="Confirmed"
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )