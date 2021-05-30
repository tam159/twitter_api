from datetime import datetime
from typing import List
from db import db


class CityModel(db.Model):
    __tablename__ = "cities"

    city_code = db.Column(db.String, primary_key=True)
    city_name = db.Column(db.String, nullable=False)
    country_code = db.Column(
        db.String, db.ForeignKey("countries.country_code"), nullable=False
    )
    country_name = db.Column(db.String, nullable=False)
    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=db.func.now(),
    )

    users = db.relationship("UserModel", backref="city", lazy="dynamic")

    def __repr__(self):
        return (
            "<City(country_code={self.country_code!r}, country_name={self.country_name!r},"
            "city_code={self.city_code!r}, city_name={self.city_name!r})>".format(
                self=self
            )
        )

    @classmethod
    def find_all(cls) -> List["CityModel"]:
        return cls.query.all()

    @classmethod
    def find_by_city_name(cls, city_name: str) -> "CityModel":
        return cls.query.filter_by(city_name=city_name).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
