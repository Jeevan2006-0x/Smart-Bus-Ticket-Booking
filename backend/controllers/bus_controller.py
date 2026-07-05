from flask import jsonify, request

# Temporary Data
buses = [
    {
        "id": 1,
        "bus_name": "KPN Travels",
        "source": "Chennai",
        "destination": "Coimbatore",
        "departure": "08:00 AM",
        "arrival": "03:00 PM",
        "price": 750
    },
    {
        "id": 2,
        "bus_name": "SRS Travels",
        "source": "Chennai",
        "destination": "Madurai",
        "departure": "09:30 AM",
        "arrival": "05:30 PM",
        "price": 680
    }
]


# -----------------------------
# Get All Buses
# -----------------------------
def get_all_buses():
    return jsonify(buses)


# -----------------------------
# Get Bus By ID
# -----------------------------
def get_bus(bus_id):

    for bus in buses:
        if bus["id"] == bus_id:
            return jsonify(bus)

    return jsonify({"message": "Bus Not Found"}), 404


# -----------------------------
# Add Bus
# -----------------------------
def add_bus():

    new_bus = request.get_json()

    buses.append(new_bus)

    return jsonify({
        "message": "Bus Added Successfully",
        "bus": new_bus
    }), 201


# -----------------------------
# Update Bus
# -----------------------------
def update_bus(bus_id):

    updated_bus = request.get_json()

    for bus in buses:

        if bus["id"] == bus_id:

            bus.update(updated_bus)

            return jsonify({
                "message": "Bus Updated Successfully",
                "bus": bus
            })

    return jsonify({"message": "Bus Not Found"}), 404


# -----------------------------
# Delete Bus
# -----------------------------
def delete_bus(bus_id):

    for bus in buses:

        if bus["id"] == bus_id:

            buses.remove(bus)

            return jsonify({
                "message": "Bus Deleted Successfully"
            })

    return jsonify({"message": "Bus Not Found"}), 404