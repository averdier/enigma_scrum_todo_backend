# coding: utf-8

import time
import os
import unittest
import subprocess
from app import create_app


class ApiUnitTestCase(unittest.TestCase):
    """Unit tests for API
    """

    def setUp(self):
        os.environ['IS_OFFLINE'] = 'True'

        self.test_app = create_app('testing')
        self.test_client = self.test_app.test_client()

        self.dynamodb_proc = subprocess.Popen(
            ['sls', 'dynamodb', 'start']
        )
        time.sleep(3)

    def tearDown(self):
        self.dynamodb_proc.terminate()
        self.dynamodb_proc.wait()

    def add_todo(self):
        response = self.test_client.post(
            '/api/todo',
            json={
                'content': 'Hello World'
            },
            follow_redirects=False
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()

        self.assertIn('content', data)
        self.assertIn('uuid', data)
        self.assertIn('created_at', data)
        self.assertEqual('Hello World', data['content'])

        return data

    def test_get_todo_list(self):
        response = self.test_client.get(
            '/api/todo',
            follow_redirects=False
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

        response = self.test_client.put(
            '/api/todo' + todo['uuid'],
            follow_redirects=False
        )

        self.assertEqual(response.status_code, 200)

    def test_delete_todo(self):
        todo = self.add_todo()

        response = self.test_client.delete(
            '/api/todo/' + todo['uuid'],
            follow_redirects=False
        )
        self.assertEqual(response.status_code, 204)
