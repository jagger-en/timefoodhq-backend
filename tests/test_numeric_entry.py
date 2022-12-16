#!/usr/bin/env python3
import unittest
from utils.base_class import BaseClass

from utils.mixins import ApiResourceTesterMixin


class TestEndpoints(ApiResourceTesterMixin, BaseClass):

    TOTAL_INITIALIZED = 5
    TEST_DATA = {
        'topic_id': '2',
        'answer': 'Chocolate',
        'value': 400,
        'date': '2022-12-05',
    }
    TEST_DATA_LIST = [
        {
            'topic_id': '2',
            'answer': 'Apples',
            'value': 400,
            'date': '2022-12-07',
        },
        {
            'topic_id': '3',
            'answer': 'Workout',
            'value': 70,
            'date': '2022-12-06',
        }
    ]

    RESOURCE_PATH = '/api/v1/numericentry'

    def _check(self, response):
        self.assertEqual(response['topic_id'], '2')
        self.assertEqual(response['answer'], 'Chocolate')
        self.assertEqual(response['value'], 400)
        self.assertEqual(response['date'], '2022-12-05')

    def _check_nested(self, response):
        self.assertEqual(response['topic']['id'], '2')
        self.assertEqual(response['answer'], 'Chocolate')
        self.assertEqual(response['value'], 400)
        self.assertEqual(response['date'], '2022-12-05')

    def _check_multiple_records(self, response):
        extracted = [{
            'topic_id': item['topic_id'],
            'answer': item['answer'],
            'value': item['value'],
            'date': item['date'],
        } for item in response.json]
        self.assertEqual(self.TEST_DATA_LIST, extracted)



if __name__ == '__main__':
    unittest.main()
