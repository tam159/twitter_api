from datetime import datetime
from typing import List
from db import db


fans = db.Table(
    "fans",
    db.Column(
        "followed_id", db.BigInteger, db.ForeignKey("users.id"), primary_key=True
    ),
    db.Column(
        "follower_id", db.BigInteger, db.ForeignKey("users.id"), primary_key=True
    ),
)


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=False)
    id_str = db.Column(db.String)
    screen_name = db.Column(db.String, unique=True)
    name = db.Column(db.String)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    profile_background_image_url = db.Column(db.Text)
    profile_background_image_url_https = db.Column(db.Text)
    profile_banner_url = db.Column(db.Text)
    profile_image_url = db.Column(db.Text)
    profile_image_url_https = db.Column(db.Text)
    profile_background_tile = db.Column(db.BOOLEAN)
    profile_use_background_image = db.Column(db.BOOLEAN)
    default_profile = db.Column(db.BOOLEAN)
    default_profile_image = db.Column(db.BOOLEAN)
    protected = db.Column(db.BOOLEAN, index=True)
    following = db.Column(db.BOOLEAN)
    verified = db.Column(db.BOOLEAN)
    contributors_enabled = db.Column(db.BOOLEAN)
    geo_enabled = db.Column(db.BOOLEAN)
    has_extended_profile = db.Column(db.BOOLEAN)
    is_translation_enabled = db.Column(db.BOOLEAN)
    is_translator = db.Column(db.BOOLEAN)
    translator_type = db.Column(db.String)
    location = db.Column(db.String)
    country_code = db.Column(db.String, db.ForeignKey("countries.country_code"))
    city_code = db.Column(db.String, db.ForeignKey("cities.city_code"), index=True)
    birthyear = db.Column(db.SmallInteger)
    age = db.Column(db.SmallInteger, index=True)
    gender = db.Column(db.String, index=True)
    ag_ai_version = db.Column(db.String)
    url = db.Column(db.String)
    entities_display_url = db.Column(db.String)
    entities_expanded_url = db.Column(db.Text)
    entities_url = db.Column(db.String)
    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=db.func.now(),
    )

    followers = db.relationship(
        "UserModel",
        secondary=fans,
        primaryjoin=(fans.c.followed_id == id),
        secondaryjoin=(fans.c.follower_id == id),
        backref=db.backref("friends", lazy="dynamic"),
        lazy="dynamic",
    )

    interests = db.relationship("UserInterestModel", backref="users", lazy="dynamic")
    user_stats = db.relationship("UserStatModel", backref="user", lazy="dynamic")
    kol = db.relationship("KolModel", backref="user", uselist=False)

    def __repr__(self):
        return "<User(id={self.id}, screen_name={self.screen_name!r})>".format(
            self=self
        )

    @classmethod
    def find_all(cls) -> List["UserModel"]:
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id: int) -> "UserModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_screen_name(cls, screen_name: str) -> "UserModel":
        return cls.query.filter_by(screen_name=screen_name).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

    def is_following(self, user):
        return (
            db.session.query(fans)
            .filter(fans.c.follower_id == self.id, fans.c.followed_id == user.id)
            .first()
        )

    def follow(self, user):
        if not self.is_following(user):
            user_tup = (
                db.session.query(UserModel.id).filter(UserModel.id == user.id).first()
            )
            if user_tup:
                db.session.execute(
                    fans.insert(), {"followed_id": user_tup.id, "follower_id": self.id}
                )
            else:
                self.friends.append(user)
            db.session.commit()
            return False
        else:
            return True

    def unfollow(self, user):
        if self.is_following(user):
            self.friends.remove(user)

    def has_follower(self, user):
        return (
            db.session.query(fans)
            .filter(fans.c.followed_id == self.id, fans.c.follower_id == user.id)
            .first()
        )

    def add_follower(self, user):
        if not self.has_follower(user):
            user_tup = (
                db.session.query(UserModel.id).filter(UserModel.id == user.id).first()
            )
            if user_tup:
                db.session.execute(
                    fans.insert(), {"followed_id": self.id, "follower_id": user_tup.id}
                )
            else:
                self.followers.append(user)
            db.session.commit()
            return False
        else:
            return True

    def remove_follower(self, user):
        if self.has_follower(user):
            self.followers.remove(user)
