from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
import json
from django.test import Client
from .models import Task

class AccountTests(APITestCase):

    def setUp(self):
        f = open('api/dataDump/data.json','r')
        data = json.load(f)
        first=Task(data=data)
        first.save()
        f.close()
        self.c = Client()

    def test_populate_model(self):
        '''
        Check if the model is created
        '''
        self.assertEqual(Task.objects.all().count(), 1)

    def test_data_model(self):
        '''
        Check if the model data is not empty
        '''
        self.assertTrue(Task.objects.first().data)

    ## Check response data and response HTTP status code of key paths requests

    def test_error_response_getData(self):
        self.assertEqual(self.c.get('/getData/').status_code, 400)

    def test_home_response(self):
        self.assertEqual(self.c.get('').status_code, 200)

    def test_error_response_badKey(self):
        response=self.c.get('/getData/', data={'key': 'ta'})
        self.assertEqual(response.status_code, 404)

    def test_error_response_goodKey(self):
        response=self.c.get('/getData/', data={'key': 'greeting'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "Hello, Carrie Summers! You have 2 unread messages.")

    def test_data_response_list(self):
        response=self.c.get('/getData/', data={'key': 'tags'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), ["duis", "minim", "culpa", "duis", "pariatur", "aute","ut"])

    def test_data_response_listIndex(self):
        response=self.c.get('/getData/', data={'key': 'tags[1]'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "minim")
    
    def test_error_response_listOutRangeKey(self):
        response=self.c.get('/getData/', data={'key': 'tags[10]'})
        self.assertEqual(response.status_code, 404)

    def test_error_response_listOutRangeBorder(self):
        response=self.c.get('/getData/', data={'key': 'friends[4]'})
        self.assertEqual(response.status_code, 404)

    def test_data_response_level(self):
        response=self.c.get('/getData/', data={'key': 'contactDetails.email'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "carriesummers@pushcart.com")

    def test_data_response_level_wrong(self):
        response=self.c.get('/getData/', data={'key': 'contactDetails.ema'})
        self.assertEqual(response.status_code, 404)

    def test_data_response_level_wrong2(self):
        response=self.c.get('/getData/', data={'key': 'contactDetails.'})
        self.assertEqual(response.status_code, 404)
    
    def test_data_response_level_wrong3(self):
        response=self.c.get('/getData/', data={'key': 'contact.emails'})
        self.assertEqual(response.status_code, 404)
    
    def test_data_response_list_and_level_wrong(self):
        response=self.c.get('/getData/', data={'key': 'friends.e'})
        self.assertEqual(response.status_code, 404)

    def test_data_response_listIndex_and_level_wrong1(self):
        response=self.c.get('/getData/', data={'key': 'friends[2].na'})
        self.assertEqual(response.status_code, 404)
    
    def test_data_response_listIndex_and_level_wrong2(self):
        response=self.c.get('/getData/', data={'key': 'tags[2].name'})
        self.assertEqual(response.status_code, 404)

    def test_data_response_listIndex_and_level_good(self):
        response=self.c.get('/getData/', data={'key': 'friends[2].name'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "Tanya Simmons")

    def test_data_response_more_levels(self):
        response=self.c.get('/getData/', data={'key': 'contactDetails.email.level3'})
        self.assertEqual(response.status_code, 404)
    
    def test_data_response_listIndex_and_levelIndex(self):
        response=self.c.get('/getData/', data={'key': 'friend[1].name[2]'})
        self.assertEqual(response.status_code, 404)

    def test_data_response_noSenseSymbol(self):
        response=self.c.get('/getData/', data={'key': '['})
        self.assertEqual(response.status_code, 404)

    def test_data_response_noSenseKey(self):
        response=self.c.get('/getData/', data={'key': 'friend.[2].first.name[1]'})
        self.assertEqual(response.status_code, 404)



