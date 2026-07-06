from database.db import db
from datetime import datetime

class Payment(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True)

    booking_id = db.Column(db.Integer, nullable=False)

    amount = db.Column(db.Float, nullable=False)

    payment_method = db.Column(db.String(50), nullable=False)

    payment_status = db.Column(db.String(50), nullable=False)

    payment_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )