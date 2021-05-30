from datetime import datetime
from typing import List
from db import db


class CountryModel(db.Model):
    __tablename__ = "countries"

    country_code = db.Column(db.String, primary_key=True)
    country_name = db.Column(db.String, nullable=False, unique=True)
    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=db.func.now(),
    )

    cities = db.relationship("CityModel", backref="country", lazy="dynamic")
    users = db.relationship("UserModel", backref="country", lazy="dynamic")

    def __repr__(self):
        return "<Country(country_code={self.country_code!r}, country_name={self.country_name!r})>".format(
            self=self
        )

    @classmethod
    def find_all(cls) -> List["CountryModel"]:
        return cls.query.all()

    @classmethod
    def find_by_country_name(cls, country_name: str) -> "CountryModel":
        return cls.query.filter_by(country_name=country_name).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
