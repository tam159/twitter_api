from datetime import datetime
from typing import List
from db import db


class InterestModel(db.Model):
    __tablename__ = "interests"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    desc = db.Column(db.String)
    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=db.func.now(),
    )

    users = db.relationship("UserInterestModel", backref="interests", lazy="dynamic")

    def __repr__(self):
        return "<Interest(name={self.name!r}, desc={self.desc!r})>".format(self=self)

    @classmethod
    def find_all(cls) -> List["InterestModel"]:
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id: int) -> "InterestModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls, name: str) -> "InterestModel":
        return cls.query.filter_by(name=name).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
