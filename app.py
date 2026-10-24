from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

app = Flask(__name__)
db = SQLAlchemy()


DB_USER = "root"  # this is naughty - we'll be replacing it with .env in production
DB_PASSWORD = "Root2026!!"
DB_HOST = "127.0.0.1"
DB_PORT = "3306"
DB_NAME = "recall"


def create_app():

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_size": 10,
        "pool_recycle": 3600,
        "pool_pre_ping": True,
    }

    db.init_app(app)

    from routes import register_routes

    register_routes(app)

    return app


# Run the local development server when this file is executed directly
