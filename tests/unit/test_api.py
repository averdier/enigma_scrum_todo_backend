# coding: utf-8

import unittest
from app import create_app


class ApiUnitTestCase(unittest.TestCase):
    """Unit tests for API
    """

    def setUp(self):
        self.test_app = create_app('testing')
        self.test_client = self.test_app.test_client()

    def test_get_todo_list(self):
        response = self.test_client.get(
            '/api/todo',
            follow_redirects=False
        )
        self.assertEqual(response.status_code, 418)

    def test_add_todo_list(self):
        response = self.test_client.post(
            '/api/todo',
            json={},
            follow_redirects=False
        )
        self.assertEqual(response.status_code, 418)

    def test_delete_todo(self):
        response = self.test_client.delete(
            '/api/todo/1',
            follow_redirects=False
        )
        self.assertEqual(response.status_code, 418)
