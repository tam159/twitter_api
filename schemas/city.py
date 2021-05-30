from ma import ma
from models.city import CityModel


class CitySchema(ma.ModelSchema):
    class Meta:
        model = CityModel
        include_relationships = True
        include_fk = True
        dump_only = ("city_code",)
