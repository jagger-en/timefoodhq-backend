import json
from functools import wraps
from sqlalchemy.exc import OperationalError
from sqlalchemy.exc import IntegrityError


def commit_wrapper(func):
    @wraps(func)
    def _commit_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs), None
        except IntegrityError as e:
            return None, f'IntegrityError Error: {e.orig}'
        except Exception as e:
            return None, f'Unknown Error: {e}'
    return _commit_wrapper


def query_wrapper(func):
    @wraps(func)
    def _query_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except OperationalError as e:
            return [], f'Operational Error: {e.orig}'
        except Exception as e:
            return [], f'Unknown Error: {e}'
    return _query_wrapper


def extract_payload(request):
    payload = request.json
    if not isinstance(payload, dict):
        payload = json.loads(payload)
    return payload
