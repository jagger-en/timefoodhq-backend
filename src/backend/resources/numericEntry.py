import datetime
from backend.models import NumericEntry
from backend.schema import NumericEntrySchema
from backend.schema import NumericEntrySchemaNested
from .api_resource import ApiResource


class NumericEntryResource(ApiResource):
    MODEL = NumericEntry
    SCHEMA = NumericEntrySchema()
    SCHEMA_NESTED = NumericEntrySchemaNested()
    SCHEMA_MANY = NumericEntrySchema(many=True)
    SCHEMA_MANY_NESTED = NumericEntrySchemaNested(many=True)

    def extract_payload(self, payload):
        try:
            payload['date'] = datetime.datetime.strptime(
                payload['date'], "%Y-%m-%d")
            return payload, None
        except Exception as e:
            return None, f'Failed to extract payload: {e}'
