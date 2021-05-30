from datetime import datetime
from typing import List
from db import db


class AgeModel(db.Model):
    __tablename__ = "ages"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer, nullable=False)
    min = db.Column(db.Integer, nullable=False)
    max = db.Column(db.Integer, nullable=False)
    desc = db.Column(db.String)
    updated_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow, server_default=db.func.now()
    )

    def __repr__(self):
        return "<Age(id={self.id}, type={self.type!r}, min={self.min}, max={self.max}, desc={self.desc!r})>".format(
            self=self
        )

    @classmethod
    def find_all(cls) -> List["AgeModel"]:
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id: int) -> "AgeModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_type(cls, type: str) -> List["AgeModel"]:
        return cls.query.filter_by(type=type).all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
