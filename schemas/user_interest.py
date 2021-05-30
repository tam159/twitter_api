from ma import ma
from models.user_interest import UserInterestModel


class UserInterestSchema(ma.ModelSchema):
    class Meta:
        model = UserInterestModel
        include_relationships = True
        include_fk = True
