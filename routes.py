from flask import Flask, jsonify, request
import pandas as pd
from werkzeug.utils import secure_filename


def register_routes(app):

    @app.route("/test")
    def home():
        return jsonify(message="Test complete.")

    @app.route("/file_upload", methods=["POST"])
    def file_upload():
        if "file" not in request.files:
            return jsonify({"error": "no file selected"}), 400

        file = request.files["file"]

        if file.filename == "":
            return jsonify({"error": "no file selected"}), 400

        if (
            file.content_type
            == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            or file.content_type == "application/vnd.ms-excel"
        ):
            file = file.save(secure_filename(file.filename))
            df = pd.read_excel(file)
            return df.to_html()

        return jsonify({"error": "wrong file type"}), 400

    @app.route("/users")
    def get_users():
        from models import User
        from app import db

        users = User.query.all()
        return jsonify("hello")
