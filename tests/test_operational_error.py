#!/usr/bin/env python3
import unittest
from utils.base_class import BaseClass
from utils.process_utils import run_command


class TestDatabaseFileRemoval(BaseClass):

    def test_table_does_not_exist(self):
        run_command(['rm', self.file_path])
        response = self.endpoint_client.get('/api/v1/topic')
        self.assertEqual(response.json, 'Operational Error: no such table: topic')

if __name__ == '__main__':
    unittest.main()
