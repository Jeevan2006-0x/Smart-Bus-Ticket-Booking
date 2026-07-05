from flask import request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

from database.db import db
from models.user import User


def register():

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    phone = data.get("phone")

    # Check existing email
    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return jsonify({
            "message": "Email already exists"
        }),400

    # Encrypt password
    hashed_password = generate_password_hash(password).decode("utf-8")

    user = User(
        name=name,
        email=email,
        password=hashed_password,
        phone=phone
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message":"User Registered Successfully"
    }),201
def login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({
            "message": "Invalid Email"
        }), 401

    if not check_password_hash(user.password, password):
        return jsonify({
            "message": "Invalid Password"
        }), 401

    access_token = create_access_token(
        identity={
            "id": user.id,
            "email": user.email,
            "role": user.role
        }
    )

    return jsonify({
        "message": "Login Successful",
        "access_token": access_token
    }), 200