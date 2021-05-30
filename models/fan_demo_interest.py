from datetime import datetime
from typing import List
from db import db


class FanDemoInterestModel(db.Model):
    __tablename__ = "fan_demo_interests"

    user_id = db.Column(db.BigInteger, db.ForeignKey("users.id"), primary_key=True)
    interest_id = db.Column(db.Integer, db.ForeignKey("interests.id"), primary_key=True)
    count = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow, server_default=db.func.now()
    )

    def __repr__(self):
        return "<FanDemoInterest(user_id={self.user_id}, interest_id={self.interest_id}, count={self.count})>".format(
            self=self
        )
