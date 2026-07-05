class Config:
    SECRET_KEY = "smart_bus_secret_key"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Jeevan%402006@localhost/smart_bus_booking"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = "smart_bus_jwt_secret"

    JWT_ACCESS_TOKEN_EXPIRES = False