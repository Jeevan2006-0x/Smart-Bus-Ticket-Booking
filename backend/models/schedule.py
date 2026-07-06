from database.db import db

class Schedule(db.Model):
    __tablename__ = "schedules"

    id = db.Column(db.Integer, primary_key=True)

    bus_id = db.Column(db.Integer, nullable=False)

    route_id = db.Column(db.Integer, nullable=False)

    departure_time = db.Column(db.DateTime, nullable=False)

    arrival_time = db.Column(db.DateTime, nullable=False)

    fare = db.Column(db.Float, nullable=False)

    available_seats = db.Column(db.Integer, nullable=False)

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )