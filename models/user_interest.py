from typing import List
from db import db


class UserInterestModel(db.Model):
    __tablename__ = "users_interests"

    user_id = db.Column(db.BigInteger, db.ForeignKey("users.id"), primary_key=True)
    interest_id = db.Column(db.Integer, db.ForeignKey("interests.id"), primary_key=True)
    value = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<UserInterest(user_id={self.user_id}, interest_id={self.interest_id}, value={self.value})>".format(
            self=self
        )

    @classmethod
    def find_all(cls) -> List["UserInterestModel"]:
        return cls.query.all()

    @classmethod
    def find_by_user_id(cls, user_id: int) -> List["UserInterestModel"]:
        return cls.query.filter_by(user_id=user_id).all()

    @classmethod
    def find_by_interest_id(cls, interest_id: int) -> List["UserInterestModel"]:
        return cls.query.filter_by(interest_id=interest_id).all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
