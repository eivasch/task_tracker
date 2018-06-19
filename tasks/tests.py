from django.test import TestCase, Client
from rest_framework import status
import json


class ApiTaskTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestCase, cls).setUpClass()
        cls.client = Client()

    @classmethod
    def tearDownClass(cls):
        super(TestCase, cls).tearDownClass()

    def test_create_task(self):
        data = {"name": "Task1",
                "project": "Project1",
                "status": "Created",
                "performer": "User1",
                "author": "User1",
                "description": ["Description1", "Description2"]}
        response = self.client.put('/tasks/create/',
                                   json.dumps(data),
                                   follow=True,
                                   content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         str(response.status_code) + " " + str(response)
                         )

        data2 = {"name": "Task2",
                 "project": "Project1",
                 "status": "Created",
                 "performer": "User2",
                 "author": "User1",
                 "description": ["Description3", "Description4"]}
        self.client.put('/tasks/create/',
                        json.dumps(data2),
                        follow=True,
                        content_type='application/json')

        data['comment'] = []

        task_pk = response.data['id']
        response = self.client.get('/tasks/info/{}'.format(task_pk), follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         str(response.status_code) + " " + str(response)
                         )

        response_data = response.data
        task_id = response_data.pop('id')

        self.assertEqual(int(task_id), int(task_pk))

        response_descriptions = response_data.pop('description')
        origin_description = data.pop('description')

        self.assertDictEqual(response_data, data)
        self.assertItemsEqual(response_descriptions, origin_description)

    def test_update_task(self):
        data = {"name": "Task1",
                "project": "Project1",
                "status": "Created",
                "performer": "User1",
                "author": "User1",
                "description": ["Description1", "Description2"]}
        response = self.client.put('/tasks/create/',
                                   json.dumps(data),
                                   follow=True,
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         str(response.status_code) + " " + str(response)
                         )
        data['comment'] = []

        task_pk = response.data['id']
        new_data = {"status": "Done", "performer": "User2"}
        response = self.client.post('/tasks/update/{}'.format(task_pk),
                                    json.dumps(new_data),
                                    follow=True,
                                    content_type='application/json')

        data.update(new_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         str(response.status_code) + " " + str(response)
                         )

        response = self.client.get('/tasks/info/{}'.format(task_pk), follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         str(response.status_code) + " " + str(response)
                         )

        response_data = response.data
        task_id = response_data.pop('id')

        self.assertEqual(int(task_id), int(task_pk))

        response_descriptions = response_data.pop('description')
        origin_description = data.pop('description')

        self.assertDictEqual(response_data, data)
        self.assertItemsEqual(response_descriptions, origin_description)

    def test_delete_task(self):
        data = {"name": "Task1",
                "project": "Project1",
                "status": "Created",
                "performer": "User1",
                "author": "User1",
                "description": ["Description1", "Description2"]}
        response = self.client.put('/tasks/create/',
                                   json.dumps(data),
                                   follow=True,
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         str(response.status_code) + " " + str(response))

        task_pk = response.data['id']
        response = self.client.delete('/tasks/delete/{}'.format(task_pk), follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         str(response.status_code) + " " + str(response)
                         )

        response = self.client.get('/tasks/info/{}'.format(task_pk), follow=True)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND,
                         str(response.status_code) + " " + str(response))

    def test_get_filtered_tasks(self):
        data = {'Task1': {"name": "Task1",
                          "project": "Project1",
                          "status": "Done",
                          "performer": "User1",
                          "author": "User1",
                          "description": ["Description1", "Description2"]},
                'Task2': {"name": "Task2",
                          "project": "Project1",
                          "status": "Created",
                          "performer": "User2",
                          "author": "User1",
                          "description": ["Description1", "Description2"]},
                'Task3': {"name": "Task3",
                          "project": "Project1",
                          "status": "Created",
                          "performer": "User3",
                          "author": "User1",
                          "description": ["Description1", "Description2"]},
                }

        for task_data in data.values():

            self.client.put('/tasks/create/',
                            json.dumps(task_data),
                            follow=True,
                            content_type='application/json')

        response = self.client.get('/tasks/filter?status=Created', follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         str(response.status_code) + " " + str(response))

        self.maxDiff = None

        for response_data in response.data:
            data['comment'] = []

            response_data.pop('id')

            response_descriptions = response_data.pop('description')
            origin_data = data[response_data['name']]
            origin_description = origin_data.pop('description')
            origin_data['comment'] = []

            self.assertDictEqual(response_data, origin_data)
            self.assertItemsEqual(response_descriptions, origin_description)
