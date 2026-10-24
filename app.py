from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
import tempfile
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)
db = SQLAlchemy()


def create_app():

    ca_cert_content = os.getenv("AIVEN_CA_CERT")

    if ca_cert_content:
        temp_ca = tempfile.NamedTemporaryFile(delete=False)
        temp_ca.write(ca_cert_content.encode("utf-8"))
        temp_ca.close()

        ssl_args = {"ssl": {"ca": temp_ca.name}}

    app.config["SQLALCHEMY_DATABASE_URI"] = f"{os.getenv('AIVEN_URI')}"

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_size": 10,
        "pool_recycle": 3600,
        "pool_pre_ping": True,
        "connect_args": ssl_args if ca_cert_content else {},
    }

    db.init_app(app)

    from routes import register_routes

    register_routes(app)

    return app


# Run the local development server when this file is executed directly
