from db import db


class TimeModel(db.Model):
    __tablename__ = "times"

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    time = db.Column(db.Time, nullable=False, unique=True)
    hour = db.Column(db.SmallInteger, nullable=False)
    hourap = db.Column(db.SmallInteger, nullable=False)
    minute = db.Column(db.Integer, nullable=False)
    second = db.Column(db.Integer, nullable=False)
    minute_of_day = db.Column(db.Integer, nullable=False)
    second_of_day = db.Column(db.Integer, nullable=False)
    quarter_hour = db.Column(db.String, nullable=False)
    am_pm = db.Column(db.String, nullable=False)
    day_night = db.Column(db.String, nullable=False)
    day_night_abbrev = db.Column(db.String, nullable=False)
    time_period = db.Column(db.String, nullable=False)
    time_period_abbrev = db.Column(db.String, nullable=False)

    user_stats = db.relationship("UserStatModel", backref="times", lazy="dynamic")

    def __repr__(self):
        return
        "<Time(id={self.id}, time={self.time})>".format(self=self)
