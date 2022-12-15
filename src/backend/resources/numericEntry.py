import datetime
from flask_restful import request
from backend.models import NumericEntry
from backend.schema import NumericEntrySchema
from .api_resource import ApiResource


class NumericEntryResource(ApiResource):
    MODEL = NumericEntry
    SCHEMA = NumericEntrySchema()
    SCHEMA_MANY = NumericEntrySchema(many=True)

    def extract_payload(self):
        try:
            payload = request.json
            payload['date'] = datetime.datetime.strptime(
                payload['date'], "%Y-%m-%d")
            return payload, None
        except Exception as e:
            return None, f'Failed to extract payload: {e}'
