from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt

from config import Config
from database.db import db

from routes.auth_routes import auth_bp
from routes.bus_routes import bus_bp

# Import models
from models.user import User
from flask_jwt_extended import JWTManager

app = Flask(__name__)
bcrypt = Bcrypt(app)
# Load Configuration
app.config.from_object(Config)

# Initialize Database
db.init_app(app)

jwt = JWTManager(app)

# Create Tables
with app.app_context():
    db.create_all()

CORS(app)

# Register Routes
app.register_blueprint(auth_bp)
app.register_blueprint(bus_bp)

@app.route("/")
def home():
    return "Smart Bus Booking Backend is Running!"

if __name__ == "__main__":
    app.run(debug=True)