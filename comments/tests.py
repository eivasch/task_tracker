from django.test import TestCase, Client
from rest_framework import status
import json


class ApiCommentTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestCase, cls).setUpClass()
        cls.client = Client()
        data = {"name": "Task2",
                "project": "Project1",
                "status": "Created",
                "performer": "User1",
                "author": "User1",
                "description": ["Description3", "Description4"]}
        response = cls.client.put('/tasks/create/',
                                  json.dumps(data),
                                  follow=True,
                                  content_type='application/json')
        cls.task_pk = int(response.data['id'])

    @classmethod
    def tearDownClass(cls):
        cls.client.delete('/tasks/delete/{}'.format(cls.task_pk))
        super(TestCase, cls).tearDownClass()

    def test_create_comment(self):
        data = {"task": self.task_pk,
                "author": "User1",
                "text": "Text1"}
        response = self.client.put('/comments/create/',
                                   json.dumps(data),
                                   follow=True,
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         str(response.status_code) + " " + str(response)
                         )

        comment_pk = response.data['id']
        response = self.client.get('/comments/info/{}'.format(comment_pk), follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         str(response.status_code) + " " + str(response)
                         )

        response_data = response.data
        comment_id = response_data.pop('id')

        self.assertEqual(int(comment_id), int(comment_pk))

        self.assertDictEqual(response_data, data)

    def test_delete_comment(self):
        data = {"task": self.task_pk,
                "author": "User1",
                "text": "Text1"}
        response = self.client.put('/comments/create/',
                                   json.dumps(data),
                                   follow=True,
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         str(response.status_code) + " " + str(response))

        comment_pk = response.data['id']
        response = self.client.delete('/comments/delete/{}'.format(comment_pk), follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         str(response.status_code) + " " + str(response)
                         )

        response = self.client.get('/comments/info/{}'.format(comment_pk), follow=True)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND,
                         str(response.status_code) + " " + str(response))
