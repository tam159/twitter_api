from datetime import datetime
from typing import List
from db import db


class FanDemoCountryModel(db.Model):
    __tablename__ = "fan_demo_countries"

    user_id = db.Column(db.BigInteger, db.ForeignKey("users.id"), primary_key=True)
    country_code = db.Column(
        db.String, db.ForeignKey("countries.country_code"), primary_key=True
    )
    count = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow, server_default=db.func.now()
    )

    def __repr__(self):
        return "<FanDemoCountry(user_id={self.user_id}, country_code={self.country_code!r}, count={self.count})>".format(
            self=self
        )
