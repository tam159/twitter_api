from ma import ma
from models.interest import InterestModel


class InterestSchema(ma.ModelSchema):
    class Meta:
        model = InterestModel
        include_relationships = True
        include_fk = True
        dump_only = ("id",)
