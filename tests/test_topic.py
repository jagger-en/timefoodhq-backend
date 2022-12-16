#!/usr/bin/env python3
import unittest
from utils.base_class import BaseClass
from utils.mixins import ApiResourceTesterMixin


class TestEndpoints(ApiResourceTesterMixin, BaseClass):
    TOTAL_INITIALIZED = 3
    TEST_DATA = {
        'name': 'EXAMPLE NAME',
        'question': 'EXAMPLE QUESTION',
        'supportedUnit': 'EXAMPLE SUPPORTED UNIT',
        'combinationOperation': 'avg',
    }
    TEST_DATA_LIST = [
        {
            'name': 'EXAMPLE NAME 1',
            'question': 'EXAMPLE QUESTION 1',
            'supportedUnit': 'EXAMPLE SUPPORTED UNIT',
            'combinationOperation': 'avg',
        },
        {
            'name': 'EXAMPLE NAME 2',
            'question': 'EXAMPLE QUESTION 2',
            'supportedUnit': 'EXAMPLE SUPPORTED UNIT',
            'combinationOperation': 'avg',
        }
    ]

    RESOURCE_PATH = '/api/v1/topic'

    def _check(self, response):
        self.assertEqual(response['name'], 'EXAMPLE NAME')
        self.assertEqual(response['question'], 'EXAMPLE QUESTION')
        self.assertEqual(response['supportedUnit'], 'EXAMPLE SUPPORTED UNIT')
        self.assertEqual(response['combinationOperation'], 'avg')

    def _check_multiple_records(self, response):
        extracted = [{
            'name': item['name'],
            'question': item['question'],
            'supportedUnit': item['supportedUnit'],
            'combinationOperation': item['combinationOperation'],
        } for item in response.json]
        self.assertEqual(self.TEST_DATA_LIST, extracted)

    def test_unique_constraint_for_name(self):
        response = self.endpoint_client.post(
            self.RESOURCE_PATH, json=self.TEST_DATA)
        response = self.endpoint_client.post(
            self.RESOURCE_PATH, json=self.TEST_DATA)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json, 'IntegrityError: UNIQUE constraint failed: topic.name')


if __name__ == '__main__':
    unittest.main()
