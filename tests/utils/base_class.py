import os
import unittest
from .data import create_test_data


class BaseClass(unittest.TestCase):

    file_path = '/tmp/tmp_test.db'

    def setUp(self):
        from backend.models.database import db  # pylint: disable=import-error
        self.db = db
        self._create_flask_app()
        self._create_database()
        self.endpoint_client = self.flask_app.test_client()

    def tearDown(self):
        os.unlink(self.file_path)

    def _create_flask_app(self):
        from backend.server import create_app  # pylint: disable=import-error
        self.flask_app = create_app({
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": f"sqlite:///{self.file_path}"})

    def _create_database(self):
        with self.flask_app.app_context():
            self.db.create_all()
            test_data = create_test_data()
            self.db.session.add_all(test_data)
            self.db.session.commit()
