from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
import json
from django.test import Client
from .models import Task

class AccountTests(APITestCase):

    def test_populate_model(self):
        """
        Ensure if Task QuerySet object is created, and populate the object model for next test

        """
        f = open('data.json','r')
        data = json.load(f)
        first=Task(data=data)
        first.save()
        f.close()
        self.assertEqual(Task.objects.all().count(), 1)
        return first

    def test_data_model(self):
        """
        Ensure the object model data is not empty
        """
        first=self.test_populate_model()
        self.assertTrue(first.data)

    def test_error_response(self):
        """
        Ensure status code of a non exist route
        """
        c = Client()
        self.assertEqual(c.get('').status_code, 404)

    def test_data_response(self):
        """
        Check if the get request reponse of list type is fine
        """
        self.test_populate_model()
        c = Client()
        response=c.get('/getData/', data={'key': 'tags'})
        self.assertEqual(response.json(), [
                                            "duis",
                                            "minim",
                                            "culpa",
                                            "duis",
                                            "pariatur",
                                            "aute",
                                            "ut"
                                        ])

    def test_data_response_listIndex(self):
        """
        Check if the get request reponse of a indexing list is fine
        """
        self.test_populate_model()
        c = Client()
        response=c.get('/getData/', data={'key': 'tags[1]'})
        self.assertEqual(response.json(), "minim")

    def test_data_response_level2(self):
        """
        Check if the get request reponse of a concatenate key is fine
        """
        self.test_populate_model()
        c = Client()
        response=c.get('/getData/', data={'key': 'contactDetails.email'})
        self.assertEqual(response.json(), "carriesummers@pushcart.com")
