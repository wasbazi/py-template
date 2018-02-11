import uuid

from sqlalchemy import Column, String, DateTime, func
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def generate_uuid():
    return str(uuid.uuid4())


class URL(db):
    id = Column(String, primary_key=True, default=generate_uuid)
    full_url = Column(String)
    short_url = Column(String)
    short_url_full = Column(String)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.utc_timestamp())

    def __repr__(self):
        return "<URL(full='%s', short='%s')>".format(self.full_url,
                                                     self.short_url)
