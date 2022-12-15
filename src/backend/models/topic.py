import uuid
import sqlalchemy as sa
from .database import db


class Topic(db.Model):
    __table_args__ = (sa.UniqueConstraint('name'), )
    id = sa.Column(sa.String(36), primary_key=True,
                   default=lambda: str(uuid.uuid4()))
    name = sa.Column(sa.String(150), nullable=False)
    contextTitle = sa.Column(sa.String(150))
    supportedUnit = sa.Column(sa.String(150))
    combinationOperation = sa.Column(sa.String(150), nullable=False)

    last_updated = sa.Column(sa.DateTime, nullable=False)

    numeric_entries = db.relationship('NumericEntry', backref='topic')
