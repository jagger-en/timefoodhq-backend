from flask_marshmallow import Marshmallow
from .topic import TopicSchema

ma = Marshmallow()


class NumericEntrySchema(ma.Schema):
    id = ma.Str()

    topic_id = ma.Str()

    answer = ma.Str()
    value = ma.Float()
    date = ma.Date()
    last_updated = ma.DateTime()


class NumericEntrySchemaNested(ma.Schema):
    id = ma.Str()

    topic = ma.Nested(TopicSchema)

    answer = ma.Str()
    value = ma.Float()
    date = ma.Date()
    last_updated = ma.DateTime()
