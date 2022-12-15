import datetime
from flask_restful import Resource, request
from backend.models import NumericEntry
from backend.models.database import db
from backend.schema import NumericEntrySchema
from backend.utils.query import query_wrapper
from backend.utils.query import extract_payload


class NumericEntryResource(Resource):

    def get(self):
        result, err = _query_all()
        if not err is None:
            return err, 404

        return result, 200

    def post(self):
        payload, err = _extract_payload(request)
        if not err is None:
            return err, 400

        new_entry = NumericEntry(**payload)
        db.session.add(new_entry)
        db.session.commit()

        new_entry_in_db = NumericEntry.query.get(new_entry.id)
        schema = NumericEntrySchema()
        return schema.dump(new_entry_in_db), 201


@query_wrapper
def _query_all():
    items = NumericEntry.query.all()
    return NumericEntrySchema(many=True).dump(items)


def _extract_payload(request):
    try:
        payload = extract_payload(request)
        payload['date'] = datetime.datetime.strptime(
            payload['date'], "%Y-%m-%d")
        return payload, None
    except Exception as e:
        return None, f'Failed to extract payload: {e}'
