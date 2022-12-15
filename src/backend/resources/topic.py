from flask_restful import Resource, request
from backend.models import Topic
from backend.schema import TopicSchema
from backend.utils.query import query_wrapper
from backend.utils.query import commit_wrapper
from backend.utils.query import extract_payload


class TopicResource(Resource):

    def get(self):
        result = _query_all()
        return result, 200

    def post(self):
        payload, err = _extract_payload(request)
        if not err is None:
            return err, 400

        new_topic, err = _add_new(payload)
        if not err is None:
            return err, 400

        new_topic_in_db = Topic.query.get(new_topic.id)
        schema = TopicSchema()
        return schema.dump(new_topic_in_db), 201


@commit_wrapper
def _add_new(payload):
    from backend.models.database import db
    new_topic = Topic(**payload)
    db.session.add(new_topic)
    db.session.commit()
    return new_topic


@query_wrapper
def _query_all():
    items = Topic.query.all()
    return TopicSchema(many=True).dump(items)


def _extract_payload(request):
    try:
        payload = extract_payload(request)
        return payload, None
    except Exception as e:
        return None, f'Failed to extract payload: {e}'
