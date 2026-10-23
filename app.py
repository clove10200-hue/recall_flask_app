from flask import Flask, jsonify, request
from sqlalchemy import SQLAlchemy
import pandas as pd

# Initialize the Flask application
app = Flask(__name__)


# Define the route for the home/root URL
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
        df = pd.read_excel(file)

    return df.to_html()


# Run the local development server when this file is executed directly
if __name__ == "__main__":
    app.run()
