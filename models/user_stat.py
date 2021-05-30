from datetime import datetime
from typing import List
from db import db


class UserStatModel(db.Model):
    __tablename__ = "user_stats"

    id = db.Column(db.BigInteger, db.ForeignKey("users.id"), primary_key=True)
    date_id = db.Column(db.Integer, db.ForeignKey("dates.id"), primary_key=True)
    time_id = db.Column(db.Integer, db.ForeignKey("times.id"), primary_key=True)
    followers_count = db.Column(db.Integer, nullable=False)
    friends_count = db.Column(db.Integer, nullable=False)
    listed_count = db.Column(db.Integer, nullable=False)
    favourites_count = db.Column(db.BigInteger, nullable=False)
    statuses_count = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=db.func.now(),
    )

    def __repr__(self):
        return "<UserStat(id={self.id}, date_id={self.date_id}, time_id={self.time_id})>".format(
            self=self
        )

    @classmethod
    def find_all(cls) -> List["UserStatModel"]:
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id: int) -> List["UserStatModel"]:
        return cls.query.filter_by(id=_id).all()

    @classmethod
    def find_by_date_id(cls, date_id: int) -> List["UserStatModel"]:
        return cls.query.filter_by(date_id=date_id).all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
