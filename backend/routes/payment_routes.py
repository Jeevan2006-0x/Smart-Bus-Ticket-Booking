from flask import Blueprint
from controllers.payment_controller import add_payment

from controllers.payment_controller import (
    add_payment,
    get_payments,
    update_payment,
    delete_payment
)

payment_bp = Blueprint("payment_bp", __name__)

payment_bp.route("/payment", methods=["POST"])(add_payment)

payment_bp.route("/payments", methods=["GET"])(get_payments)

payment_bp.route("/payment/<int:id>", methods=["PUT"])(update_payment)

payment_bp.route("/payment/<int:id>", methods=["DELETE"])(delete_payment)