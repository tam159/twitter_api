from ma import ma
from models.user_stat import UserStatModel


class UserStatSchema(ma.ModelSchema):
    class Meta:
        model = UserStatModel
        include_relationships = True
        include_fk = True
