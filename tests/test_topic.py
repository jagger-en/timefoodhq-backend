#!/usr/bin/env python3
import unittest
from utils.base_class import BaseClass


class TestEndpoints(BaseClass):
    def test_all_topics_shown(self):
        response = self.endpoint_client.get('/api/v1/topic')
        self.assertEqual(len(response.json), 3)

    def test_adding_topic(self):
        def _check(response):
            self.assertEqual(response['name'], 'EXAMPLE NAME')
            self.assertEqual(response['contextTitle'], 'EXAMPLE CONTEXT TITLE')
            self.assertEqual(response['supportedUnit'], 'EXAMPLE SUPPORTED UNIT')
            self.assertEqual(response['combinationOperation'], 'avg')

        response = self.endpoint_client.post('/api/v1/topic', json={
            'name': 'EXAMPLE NAME',
            'contextTitle': 'EXAMPLE CONTEXT TITLE',
            'supportedUnit': 'EXAMPLE SUPPORTED UNIT',
            'combinationOperation': 'avg',
        })
        self.assertEqual(response.status_code, 201)
        _check(response.json)

        response = self.endpoint_client.get('/api/v1/topic')
        self.assertEqual(response.status_code, 200)
        _check([item for item in response.json if item['name'] == 'EXAMPLE NAME'][0])


if __name__ == '__main__':
    unittest.main()
