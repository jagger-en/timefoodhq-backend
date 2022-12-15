import uuid
import sqlalchemy as sa
from .database import db


class Topic(db.Model):
    id = sa.Column(sa.String(36), primary_key=True,
                   default=lambda: str(uuid.uuid4()))
    name = sa.Column(sa.String(150), nullable=False)
    contextTitle = sa.Column(sa.String(150))
    supportedUnit = sa.Column(sa.String(150))
    combinationOperation = sa.Column(sa.String(150), nullable=False)

    numeric_entries = db.relationship('NumericEntry', backref='topic')
