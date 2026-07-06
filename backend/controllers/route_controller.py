from flask import request, jsonify
from database.db import db
from models.route import Route


def add_route():
    data = request.get_json()

    from_city = data.get("from_city")
    to_city = data.get("to_city")
    distance = data.get("distance")

    existing_route = Route.query.filter_by(
        from_city=from_city,
        to_city=to_city
    ).first()

    if existing_route:
        return jsonify({
            "message": "Route already exists"
        }), 400

    route = Route(
        from_city=from_city,
        to_city=to_city,
        distance=distance
    )

    db.session.add(route)
    db.session.commit()

    return jsonify({
        "message": "Route Added Successfully"
    }), 201


def get_routes():

    routes = Route.query.all()

    output = []

    for route in routes:
        output.append({
            "id": route.id,
            "from_city": route.from_city,
            "to_city": route.to_city,
            "distance": route.distance
        })

    return jsonify(output), 200