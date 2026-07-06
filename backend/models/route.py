from database.db import db

class Route(db.Model):
    __tablename__ = "routes"

    id = db.Column(db.Integer, primary_key=True)

    from_city = db.Column(db.String(100), nullable=False)

    to_city = db.Column(db.String(100), nullable=False)

    distance = db.Column(db.Integer, nullable=False)

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )