import datetime
from flask_restful import Resource, request
from backend.models.database import db
from backend.utils.query import query_wrapper
from backend.utils.query import commit_wrapper


class ApiResource(Resource):

    NOT_FOUND = "Resource with id=%s not found"

    MODEL = None
    SCHEMA = None
    SCHEMA_MANY = None

    def get(self):
        form_data = dict(request.args)
        if form_data.get('id'):
            item = self.MODEL.query.get(form_data.get('id'))
            if item:
                return self.SCHEMA.dump(item), 200
            return self.NOT_FOUND % form_data.get('id'), 404

        result, err = self._query_all()
        if not err is None:
            return err, 404

        return result, 200

    def post(self):
        request_json = request.json
        if type(request_json) == dict:
            return self.handle_single_entry(request_json)
        if type(request_json) == list:
            return self.handle_multiple_entries(request_json)
        return "Failed to parse payload", 400

    def handle_single_entry(self, payload):
        payload, err = self.extract_payload(payload)
        if not err is None:
            return err, 400

        new_record, err = self._add_new(payload)
        if not err is None:
            return err, 400

        new_record_from_db = self.MODEL.query.get(new_record.id)
        return self.SCHEMA.dump(new_record_from_db), 201

    def handle_multiple_entries(self, payload):
        '''
        NOTE: If one of the records fail to be added, we must
              abort the session without committing partially.
        '''
        new_entries = []
        for entry in payload:
            resp, resp_code = self.handle_single_entry(entry)
            if resp_code != 201:
                return resp, resp_code
            new_entries.append(resp)
        return new_entries, 201

    def delete(self):
        form_data = dict(request.args)
        if form_data.get('id'):
            item = self.MODEL.query.get(form_data.get('id'))
            if item:
                db.session.delete(item)
                db.session.commit()
                return self.SCHEMA.dump(item), 200
            return self.NOT_FOUND % form_data.get('id'), 404
        return "Resource id must be given", 400

    @query_wrapper
    def _query_all(self):
        items = self.MODEL.query.order_by(self.MODEL.last_updated.desc()).all()
        return self.SCHEMA_MANY.dump(items)

    @commit_wrapper
    def _add_new(self, payload):
        from backend.models.database import db

        payload['last_updated'] = datetime.datetime.now()
        new_record = self.MODEL(**payload)
        db.session.add(new_record)
        db.session.commit()
        return new_record

    def extract_payload(self, payload):
        '''Overrideable method'''
        return payload, None
