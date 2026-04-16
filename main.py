from flask import Flask, jsonify
from models import Distro
from extensions import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///distros.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return jsonify(
        {"message": "Hello, Linux!"}
    )

if __name__ == "__main__":
    app.run(debug=True)