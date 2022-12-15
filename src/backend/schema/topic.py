from flask_marshmallow import Marshmallow

ma = Marshmallow()


class TopicSchema(ma.Schema):
    id = ma.Str()
    name = ma.Str()
    contextTitle = ma.Str()
    supportedUnit = ma.Str()
    combinationOperation = ma.Str()
    last_updated = ma.DateTime()
