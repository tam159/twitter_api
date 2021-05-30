from db import db
from models.user import UserModel
from schemas.user import UserSchema
from schemas.city import CitySchema
from schemas.country import CountrySchema
from schemas.kol import KolSchema

# user_schema = UserSchema()

# user_json = {
#     "id": 1234,
# "screen_name": "npt_dc"
# }

# user = user_schema.load(user_json)


kol_schema = KolSchema()

kol_json = {
    # "screen_name":"npt_dc",
    "priority": 10,
    "phone": 968985355,
    "full_name": "Nguyen Phuc Tam",
    "email": "npt.dc93@gmail.com",
}

kol = kol_schema.load(kol_json)
print(type(kol))
print(kol)

# city_schema = CitySchema()

# city_json = {
#     "city_code": "hala",
#     "city_name": "halaname",
#     "country_code": "bu",
#     "country_name": "burundi"
# }

# city = city_schema.load(city_json)
# print(city)

country_schema = CountrySchema()

country_json = {
    # "country_code": "bu",
    "country_name": "burundi"
}

country = country_schema.load(country_json)
print(country)
print(type(country))
