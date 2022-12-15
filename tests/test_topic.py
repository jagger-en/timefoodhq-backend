#!/usr/bin/env python3
import unittest
from utils.base_class import BaseClass
from utils.mixins import ApiResourceTesterMixin


class TestEndpoints(ApiResourceTesterMixin, BaseClass):
    TOTAL_INITIALIZED = 3
    TEST_DATA = {
        'name': 'EXAMPLE NAME',
        'contextTitle': 'EXAMPLE CONTEXT TITLE',
        'supportedUnit': 'EXAMPLE SUPPORTED UNIT',
        'combinationOperation': 'avg',
    }

    RESOURCE_PATH = '/api/v1/topic'

    def _check(self, response):
        self.assertEqual(response['name'], 'EXAMPLE NAME')
        self.assertEqual(response['contextTitle'], 'EXAMPLE CONTEXT TITLE')
        self.assertEqual(response['supportedUnit'], 'EXAMPLE SUPPORTED UNIT')
        self.assertEqual(response['combinationOperation'], 'avg')

    def test_unique_constraint_for_name(self):
        response = self.endpoint_client.post(
            self.RESOURCE_PATH, json=self.TEST_DATA)
        response = self.endpoint_client.post(
            self.RESOURCE_PATH, json=self.TEST_DATA)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json, 'IntegrityError Error: UNIQUE constraint failed: topic.name')


if __name__ == '__main__':
    unittest.main()
