import os

from flask import Flask, jsonify
from flask_restful import Api
from flask_migrate import Migrate
from marshmallow import ValidationError
from dotenv import load_dotenv

from db import db
from ma import ma

from resources.kol import Kol, KolList
from resources.user import User, UserScreenName


app = Flask(__name__)
load_dotenv(".env")
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
api = Api(app)
migrate = Migrate(app, db)


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


api.add_resource(Kol, "/kol/<string:screen_name>", methods=["GET", "POST", "PUT"])
api.add_resource(KolList, "/kols")
api.add_resource(User, "/user/<int:_id>", methods=["GET"])
api.add_resource(
    UserScreenName, "/user/screen_name/<string:screen_name>", methods=["GET"]
)


def create_app():
    db.init_app(app)
    ma.init_app(app)
    return app
