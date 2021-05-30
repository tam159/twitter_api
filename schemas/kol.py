from ma import ma
from models.kol import KolModel


class KolSchema(ma.ModelSchema):
    class Meta:
        model = KolModel
        include_relationships = True
        include_fk = True
        dump_only = ("screen_name",)
