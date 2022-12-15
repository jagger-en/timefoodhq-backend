#!/usr/bin/env python3
import unittest
from utils.base_class import BaseClass


class TestEndpoints(BaseClass):
    TEST_DATA = {
        'name': 'EXAMPLE NAME',
        'contextTitle': 'EXAMPLE CONTEXT TITLE',
        'supportedUnit': 'EXAMPLE SUPPORTED UNIT',
        'combinationOperation': 'avg',
    }

    def _check(self, response):
        self.assertEqual(response['name'], 'EXAMPLE NAME')
        self.assertEqual(response['contextTitle'], 'EXAMPLE CONTEXT TITLE')
        self.assertEqual(response['supportedUnit'], 'EXAMPLE SUPPORTED UNIT')
        self.assertEqual(response['combinationOperation'], 'avg')

    def test_all_topics_shown(self):
        response = self.endpoint_client.get('/api/v1/topic')
        self.assertEqual(len(response.json), 3)

    def test_adding_topic(self):
        response = self.endpoint_client.post(
            '/api/v1/topic', json=self.TEST_DATA)
        self.assertEqual(response.status_code, 201)
        self._check(response.json)
        topic_id = response.json['id']

        response = self.endpoint_client.get('/api/v1/topic?id=%s' % topic_id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], topic_id)
        self._check(response.json)

    def test_404(self):
        response = self.endpoint_client.get('/api/v1/topic?id=%s' % 'foo-bar')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, "Topic with id=foo-bar not found")

    def test_unique_constraint_for_name(self):
        response = self.endpoint_client.post(
            '/api/v1/topic', json=self.TEST_DATA)
        response = self.endpoint_client.post(
            '/api/v1/topic', json=self.TEST_DATA)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json, 'IntegrityError Error: UNIQUE constraint failed: topic.name')


if __name__ == '__main__':
    unittest.main()
