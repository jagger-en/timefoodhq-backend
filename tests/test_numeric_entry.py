#!/usr/bin/env python3
import unittest
from utils.base_class import BaseClass

from utils.mixins import ApiResourceTesterMixin


class TestEndpoints(ApiResourceTesterMixin, BaseClass):

    TOTAL_INITIALIZED = 5
    TEST_DATA = {
        'topic_id': 2,
        'answer': 'Chocolate',
        'value': 400,
        'date': '2022-12-05',
    }

    RESOURCE_PATH = '/api/v1/numericentry'

    def _check(self, response):
        self.assertEqual(response['topic']['id'], '2')
        self.assertEqual(response['answer'], 'Chocolate')
        self.assertEqual(response['value'], 400)
        self.assertEqual(response['date'], '2022-12-05')


if __name__ == '__main__':
    unittest.main()
