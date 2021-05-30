from flask_restful import Resource
from flask import request
from models.kol import KolModel
from schemas.kol import KolSchema

KOL_ALREADY_EXISTS = "A kol with screen_name={} already exists."
KOL_NOT_FOUND = "Kol not found."
KOL_DELETED = "Kol deleted."

kol_schema = KolSchema()
kol_list_schema = KolSchema(many=True)


class Kol(Resource):
    @classmethod
    def get(cls, screen_name: str):
        kol = KolModel.find_by_screen_name(screen_name)
        if kol:
            return kol_schema.dump(kol), 200

        return {"message": KOL_NOT_FOUND}, 404

    @classmethod
    def post(cls, screen_name: str):
        if KolModel.find_by_screen_name(screen_name):
            return {"message": KOL_ALREADY_EXISTS.format(screen_name)}, 400

        kol_json = request.get_json()

        kol = kol_schema.load(kol_json)
        kol.screen_name = screen_name.lower()

        kol.save_to_db()

        print(kol)
        return kol_schema.dump(kol), 201

    @classmethod
    def delete(cls, screen_name: str):
        kol = KolModel.find_by_screen_name(screen_name)
        if kol:
            kol.delete_from_db()
            return {"message": KOL_DELETED}, 200

        return {"message": KOL_NOT_FOUND}, 404

    @classmethod
    def put(cls, screen_name: str):
        kol_json = request.get_json()
        kol = KolModel.find_by_screen_name(screen_name)

        if kol:
            kol.priority = kol_json["priority"]
        else:
            kol = kol_schema.load(kol_json)
            kol.screen_name = screen_name.lower()

        kol.save_to_db()

        return kol_schema.dump(kol), 200


class KolList(Resource):
    @classmethod
    def get(cls):
        return {"kols": kol_list_schema.dump(KolModel.find_all())}, 200
