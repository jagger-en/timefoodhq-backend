#!/usr/bin/env python3
import unittest
from utils.base_class import BaseClass


class TestEndpoints(BaseClass):
    def test_all_numericentrys_shown(self):
        response = self.endpoint_client.get('/api/v1/numericentry')
        self.assertEqual(len(response.json), 5)

    def test_adding_numericentry(self):
        response = self.endpoint_client.post('/api/v1/numericentry', json={
            'topic_id': 2,
            'context': 'Chocolate',
            'value': 400,
            'date': '2022-12-05',
        })

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['context'], 'Chocolate')
        self.assertEqual(response.json['value'], 400)
        self.assertEqual(response.json['topic']['name'], 'Food spending')
        entry_id = response.json['id']

        response = self.endpoint_client.get(
            '/api/v1/numericentry?id=%s' % entry_id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], entry_id)
        self.assertEqual(response.json['topic']['name'], 'Food spending')

    def test_404(self):
        response = self.endpoint_client.get(
            '/api/v1/numericentry?id=%s' % 'foo-bar')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.json, "Resource with id=foo-bar not found")

    def test_deleting_numericentry(self):
        response = self.endpoint_client.post('/api/v1/numericentry', json={
            'topic_id': 2,
            'context': 'Potato Chips',
            'value': 400,
            'date': '2022-12-05',
        })
        entry_id = response.json['id']

        response = self.endpoint_client.delete('/api/v1/numericentry', json={
            'id': entry_id,
        })
        self.assertEqual(response.status_code, 200)

        response = self.endpoint_client.get(
            '/api/v1/numericentry?id=%s' % entry_id)
        self.assertEqual(response.status_code, 404)

    def test_delete_request_for_non_existing_resource(self):
        response = self.endpoint_client.delete('/api/v1/numericentry', json={
            'id': 'non-existing-123'
        })
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, "Resource with id=non-existing-123 not found")

    def test_delete_request_without_id(self):
        response = self.endpoint_client.delete('/api/v1/numericentry', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, "Resource id must be given")


if __name__ == '__main__':
    unittest.main()
