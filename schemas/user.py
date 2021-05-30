from ma import ma
from models.user import UserModel


class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        include_relationships = True
        include_fk = True
        dump_only = ("id",)
