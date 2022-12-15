class MissingAttribute(Exception):
    pass


class ApiResourceTesterMixin():
    TOTAL_INITIALIZED = None
    TEST_DATA = None
    RESOURCE_PATH = None

    ##############
    # HTTP: GET
    ###

    def test_all_shown(self):
        response = self.get_all()
        self.assertEqual(len(response.json), self.TOTAL_INITIALIZED)

    def test_404(self):
        if self.RESOURCE_PATH is None:
            raise MissingAttribute('RESOURCE_PATH')

        response = self.endpoint_client.get(
            '%s?id=%s' % (self.RESOURCE_PATH, 'foo-bar'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, "Resource with id=foo-bar not found")

    ##############
    # HTTP: POST
    ###

    def test_adding_new_record(self):
        if self.TEST_DATA is None:
            raise MissingAttribute('TEST_DATA')
        if self.RESOURCE_PATH is None:
            raise MissingAttribute('RESOURCE_PATH')

        response = self.post_test_data()
        record_id = response.json['id']
        self.assertEqual(response.status_code, 201)
        self._check(response.json)

        response = self.get_resource_by_id(record_id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], record_id)
        self._check(response.json)

    ##############
    # HTTP: DELETE
    ###

    def test_deleting_resource(self):
        response = self.post_test_data()
        record_id = response.json['id']

        response = self.delete_resource_by_id(record_id)
        self.assertEqual(response.status_code, 200)

        response = self.get_resource_by_id(record_id)
        self.assertEqual(response.status_code, 404)

    def test_delete_request_for_non_existing_resource(self):
        response = self.delete_resource_by_id('non-existing-123')

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.json, "Resource with id=non-existing-123 not found")

    def test_delete_request_without_id(self):
        response = self.endpoint_client.delete(self.RESOURCE_PATH, json={})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, "Resource id must be given")

    ##############
    # Helper Methods
    ###

    def get_all(self):
        return self.endpoint_client.get(self.RESOURCE_PATH)

    def get_resource_by_id(self, record_id):
        return self.endpoint_client.get('%s?id=%s' % (self.RESOURCE_PATH, record_id))

    def post_test_data(self):
        return self.endpoint_client.post(self.RESOURCE_PATH, json=self.TEST_DATA)

    def delete_resource_by_id(self, record_id):
        payload = {'id': record_id}
        return self.endpoint_client.delete(self.RESOURCE_PATH, json=payload)
