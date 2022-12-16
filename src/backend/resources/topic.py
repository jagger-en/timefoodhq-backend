from backend.models import Topic
from backend.schema import TopicSchema
from .api_resource import ApiResource


class TopicResource(ApiResource):
    MODEL = Topic
    SCHEMA = TopicSchema()
    SCHEMA_NESTED = TopicSchema()
    SCHEMA_MANY = TopicSchema(many=True)
    SCHEMA_MANY_NESTED = TopicSchema(many=True)
