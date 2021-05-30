from datetime import datetime
from typing import List
from db import db


class FanDemoGenderModel(db.Model):
    __tablename__ = "fan_demo_genders"

    user_id = db.Column(db.BigInteger, db.ForeignKey("users.id"), primary_key=True)
    males_count = db.Column(db.Integer, nullable=False)
    females_count = db.Column(db.Integer, nullable=False)
    null_count = db.Column(db.Integer)
    updated_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow, server_default=db.func.now()
    )

    def __repr__(self):
        return "<FanDemoGender(user_id={self.user_id}, males_count={self.males_count}, females_count={self.females_count})>".format(
            self=self
        )
