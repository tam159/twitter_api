from typing import List
from db import db
from datetime import datetime


class KolModel(db.Model):
    __tablename__ = "kols"

    screen_name = db.Column(db.String, primary_key=True)
    id = db.Column(db.BigInteger, db.ForeignKey("users.id"), unique=True)
    full_name = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.BigInteger)
    priority = db.Column(db.Integer)
    crawled_profile = db.Column(db.BOOLEAN)
    error_code = db.Column(db.Integer)
    error = db.Column(db.String)
    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=db.func.now(),
    )
    fans_ids_count = db.Column(db.Integer)
    fans_ids_last_crawled = db.Column(db.DateTime)
    fans_profiles_count = db.Column(db.Integer)
    fans_profiles_last_crawled = db.Column(db.DateTime)

    def __repr__(self):
        return "<Kol(screen_name={self.screen_name!r}, id={self.id})>".format(self=self)

    @classmethod
    def find_all(cls) -> List["KolModel"]:
        return cls.query.all()

    @classmethod
    def find_by_screen_name(cls, screen_name: str) -> "KolModel":
        return cls.query.filter_by(screen_name=screen_name.lower()).first()

    @classmethod
    def find_by_id(cls, _id: int) -> "KolModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
