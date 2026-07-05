from flask import jsonify

# Temporary data
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

def get_all_buses():
    return jsonify(buses)