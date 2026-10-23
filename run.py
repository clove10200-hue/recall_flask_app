from app import create_app

app = create_app()[0]

if __name__ == "__main__":
    app.run(debug=True)
