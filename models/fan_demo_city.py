from datetime import datetime
from typing import List
from db import db


class FanDemoCityModel(db.Model):
    __tablename__ = "fan_demo_cities"

    user_id = db.Column(db.BigInteger, db.ForeignKey("users.id"), primary_key=True)
    city_code = db.Column(db.String, db.ForeignKey("cities.city_code"), primary_key=True)
    count = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow, server_default=db.func.now()
    )

    def __repr__(self):
        return "<FanDemoCity(user_id={self.user_id}, city_code={self.city_code!r}, count={self.count})>".format(
            self=self
        )
