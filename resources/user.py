from flask_restful import Resource
from flask import request
from models.user import UserModel
from schemas.user import UserSchema

USER_ALREADY_EXISTS = "A user with id={} already exists."
USER_NOT_FOUND = "User not found."
USER_DELETED = "User deleted."

user_schema = UserSchema()
user_list_schema = UserSchema(many=True)


class User(Resource):
    @classmethod
    def get(cls, _id: int):
        user = UserModel.find_by_id(_id)
        if user:
            return user_schema.dump(user), 200

        return {"message": USER_NOT_FOUND}, 404

    @classmethod
    def post(cls, _id: int):
        if UserModel.find_by_id(_id):
            return {"message": USER_ALREADY_EXISTS.format(_id)}, 400

        user_json = request.get_json()

        user = user_schema.load(user_json)
        user.id = _id

        user.save_to_db()

        return user_schema.dump(user), 201

    @classmethod
    def delete(cls, _id: int):
        user = UserModel.find_by_id(_id)
        if user:
            user.delete_from_db()
            return {"message": USER_DELETED}, 200

        return {"message": USER_NOT_FOUND}, 404


class UserScreenName(Resource):
    @classmethod
    def get(cls, screen_name: str):
        user = UserModel.find_by_screen_name(screen_name)
        if user:
            return user_schema.dump(user), 200

        return {"message": USER_NOT_FOUND}, 404


class UserList(Resource):
    @classmethod
    def get(cls):
        return {"users": user_list_schema.dump(UserModel.find_all())}, 200
