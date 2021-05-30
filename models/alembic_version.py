from db import db


class AlembicVersionModel(db.Model):
    __tablename__ = "alembic_version"

    version_num = db.Column(db.String, primary_key=True)
