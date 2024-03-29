from functools import wraps
from sqlalchemy.exc import OperationalError
from sqlalchemy.exc import IntegrityError
from .exceptions import FailedToHandlePostRequest


def commit_wrapper(func):
    @wraps(func)
    def _commit_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs), None
        except IntegrityError as e:
            return None, f'IntegrityError: {e.orig}'
        except OperationalError as e:
            return None, f'OperationalError: {e.orig}'
        except FailedToHandlePostRequest as e:
            return None, f'FailedToHandlePostRequest: {e}'
        except Exception as e:
            return None, f'Unknown Error: {e}'
    return _commit_wrapper


def query_wrapper(func):
    @wraps(func)
    def _query_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs), None
        except OperationalError as e:
            return None, f'Operational Error: {e.orig}'
        except Exception as e:
            return None, f'Unknown Error: {e}'
    return _query_wrapper
