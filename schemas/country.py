from ma import ma
from models.country import CountryModel


class CountrySchema(ma.ModelSchema):
    class Meta:
        model = CountryModel
        include_relationships = True
        include_fk = True
        dump_only = ("country_code",)
