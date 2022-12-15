import uuid
import sqlalchemy as sa
from .database import db


class NumericEntry(db.Model):
    id = sa.Column(sa.String(36), primary_key=True,
                   default=lambda: str(uuid.uuid4()))
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    context = sa.Column(sa.String(150))
    value = sa.Column(sa.Float, nullable=False)
    date = sa.Column(sa.Date, nullable=False)
