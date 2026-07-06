from database.db import db

class Bus(db.Model):
    __tablename__ = "buses"

    id = db.Column(db.Integer, primary_key=True)
    bus_number = db.Column(db.String(20), unique=True, nullable=False)
    bus_name = db.Column(db.String(100), nullable=False)
    bus_type = db.Column(db.String(50))
    total_seats = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())