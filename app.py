from flask import Flask, jsonify

# Initialize the Flask application
app = Flask(__name__)


# Define the route for the home/root URL
@app.route("/test")
def home():
    return jsonify(message="Test complete.")


# Run the local development server when this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)
