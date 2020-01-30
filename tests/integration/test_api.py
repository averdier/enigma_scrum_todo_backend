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

    def add_todo(self):
        response = requests.post(
            self.todo_backend + '/api/todo',
            json={
                'content': 'Hello World'
            }
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()

        self.assertIn('content', data)
        self.assertIn('uuid', data)
        self.assertIn('created_at', data)
        self.assertEqual('Hello World', data['content'])

        return data

    def test_get_todo_list(self):
        response = requests.get(
            self.todo_backend + '/api/todo',
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()

        self.assertIn('todos', data)
        self.assertIn('pagination', data)
        self.assertIn('current', data['pagination'])
        self.assertIn('next', data['pagination'])
        self.assertIn('limit', data['pagination'])

    def test_add_todo_list(self):
        self.add_todo()

    def test_put_todo(self):
        todo = self.add_todo()

        response = requests.put(
            self.todo_backend + '/api/todo/' + todo['uuid'],
            json={
                'content': 'Updated hello world'
            }
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()

        self.assertEqual(data['content'], 'Updated hello world')

    def test_delete_todo(self):
        todo = self.add_todo()

        response = requests.delete(
            self.todo_backend + '/api/todo/' + todo['uuid']
        )
        self.assertEqual(response.status_code, 204)
