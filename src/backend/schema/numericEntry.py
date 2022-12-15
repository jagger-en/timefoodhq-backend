from flask_marshmallow import Marshmallow
from .topic import TopicSchema

ma = Marshmallow()


class NumericEntrySchema(ma.Schema):
    id = ma.Str()

    topic = ma.Nested(TopicSchema)

    context = ma.Str()
    value = ma.Float()
    date = ma.Date()
