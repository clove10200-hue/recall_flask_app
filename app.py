from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import tempfile
from werkzeug.utils import secure_filename

load_dotenv()

app = Flask(__name__)
CORS(app)
db = SQLAlchemy()


def create_app():

    # ca_cert_content = os.getenv("AIVEN_CA_CERT")

    # if ca_cert_content:
    #    temp_ca = tempfile.NamedTemporaryFile(delete=False)
    #    temp_ca.write(ca_cert_content.encode("utf-8"))
    #    temp_ca.close()

    #    ssl_args = {"ssl": {"ca": temp_ca.name}}

    app.config["SQLALCHEMY_DATABASE_URI"] = f"{os.getenv('AIVEN_URI')}"

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_size": 10,
        "pool_recycle": 3600,
        "pool_pre_ping": True,
        "connect_args": {
            "ssl": {"ca": os.path.join(os.path.dirname(__file__), "ca.pem")}
        },
    }

    db.init_app(app)

    from routes import register_routes

    register_routes(app)

    return app


# Run the local development server when this file is executed directly
