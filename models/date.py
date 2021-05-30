from db import db


class DateModel(db.Model):
    __tablename__ = "dates"

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    date = db.Column(db.Date, nullable=False, unique=True)
    epoch = db.Column(db.Float, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    quarter = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)
    day = db.Column(db.Integer, nullable=False)
    quarter_month_day = db.Column(db.Integer, nullable=False)
    month_day = db.Column(db.Integer, nullable=False)
    month_name = db.Column(db.String, nullable=False)
    month_abbrev = db.Column(db.String, nullable=False)
    weekday_name = db.Column(db.String, nullable=False)
    weekday_abbrev = db.Column(db.String, nullable=False)
    week_in_month = db.Column(db.Integer, nullable=False)
    week_in_year = db.Column(db.Integer, nullable=False)
    day_in_week = db.Column(db.Integer, nullable=False)
    day_in_year = db.Column(db.Integer, nullable=False)
    is_working_day = db.Column(db.Boolean, nullable=False)
    year_in_dimension = db.Column(db.Integer, nullable=False)
    month_in_dimension = db.Column(db.Integer, nullable=False)
    day_in_dimension = db.Column(db.Integer, nullable=False)
    iso_year = db.Column(db.Integer, nullable=False)
    iso_week_in_year = db.Column(db.Integer, nullable=False)
    iso_day_in_year = db.Column(db.Integer, nullable=False)
    iso_day_in_week = db.Column(db.Integer, nullable=False)

    user_stats = db.relationship("UserStatModel", backref="dates", lazy="dynamic")

    def __repr__(self):
        return
        "<Date(id={self.id}, date={self.date})>".format(self=self)
