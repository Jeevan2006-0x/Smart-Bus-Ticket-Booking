from flask import request, jsonify
from database.db import db
from models.payment import Payment


def add_payment():
    data = request.get_json()

    payment = Payment(
        booking_id=data["booking_id"],
        amount=data["amount"],
        payment_method=data["payment_method"],
        payment_status=data["payment_status"]
    )

    db.session.add(payment)
    db.session.commit()

    return jsonify({
        "message": "Payment created successfully"
    }), 201

def get_payments():
    payments = Payment.query.all()

    result = []

    for payment in payments:
        result.append({
            "id": payment.id,
            "booking_id": payment.booking_id,
            "amount": payment.amount,
            "payment_method": payment.payment_method,
            "payment_status": payment.payment_status,
            "payment_date": str(payment.payment_date)
        })

    return jsonify(result), 200

def update_payment(id):
    data = request.get_json()

    payment = Payment.query.get(id)

    if not payment:
        return jsonify({"message": "Payment not found"}), 404

    payment.booking_id = data["booking_id"]
    payment.amount = data["amount"]
    payment.payment_method = data["payment_method"]
    payment.payment_status = data["payment_status"]

    db.session.commit()

    return jsonify({
        "message": "Payment updated successfully"
    }), 200

def delete_payment(id):
    payment = Payment.query.get(id)

    if not payment:
        return jsonify({"message": "Payment not found"}), 404

    db.session.delete(payment)
    db.session.commit()

    return jsonify({
        "message": "Payment deleted successfully"
    }), 200