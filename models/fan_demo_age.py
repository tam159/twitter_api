from datetime import datetime
from typing import List
from db import db


class FanDemoAgeModel(db.Model):
    __tablename__ = "fan_demo_ages"

    user_id = db.Column(db.BigInteger, db.ForeignKey("users.id"), primary_key=True)
    age_id = db.Column(db.Integer, db.ForeignKey("ages.id"), primary_key=True)
    count = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow, server_default=db.func.now()
    )

    def __repr__(self):
        return "<FanDemoAge(user_id={self.user_id}, age_id={self.age_id}, count={self.count})>".format(
            self=self
        )
