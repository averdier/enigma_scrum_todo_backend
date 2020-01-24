# coding: utf-8

import os
import unittest
import requests


class ApiIntegrationTestCase(unittest.TestCase):

    def setUp(self):
        self.todo_backend = os.getenv(
            'TODO_BACKEND',
            'https://q05hqiwa26.execute-api.eu-central-1.amazonaws.com/dev'
        )

    def test_get_todo_list(self):
        response = requests.get(
            self.todo_backend + '/api/todo',
        )
        self.assertEqual(response.status_code, 418)

    def test_add_todo_list(self):
        response = requests.post(
            self.todo_backend + '/api/todo', {}
        )
        self.assertEqual(response.status_code, 418)

    def test_delete_todo(self):
        response = requests.delete(
            self.todo_backend + '/api/todo/1',
        )
        self.assertEqual(response.status_code, 418)
