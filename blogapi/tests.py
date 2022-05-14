import email
from urllib import response
from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase 
from baseapp.models import User, Post


class TESTAPI(APITestCase):
    def test_get(self):
        url = reverse('posts')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        user1 = User(username='oboo', email='obide2@yahoo.com', password='1234567892')
        user1.save()
        url = reverse('posts')
        data = {"name": "javascript", "description": "is  cool", "author": 1}
        data2 = {
        "name": "Apaches",
        "description": "both ko",
        "author": 1
        }
        response = self.client.post(url, data2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)    

    def test_delete(self):
        user1 = User(username='oboo', email='obide2@yahoo.com', password='1234567892')
        user1.save()
        url = reverse('detailled_view', args=[1])
        print(url)
        post = Post(name="javascript", description="is  cool", author=user1)
        post.save()
        response = self.client.delete(url)
        self.assertEqual(response.data, 'post was deleted succesfully')

    def test_update(self):
        user1 = User(username='oboo', email='obide2@yahoo.com', password='1234567892')
        user1.save()
        url = reverse('detailled_view', args=[1])
        print(url)
        post = Post(name="javascript", description="is  cool", author=user1)
        post.save()
        data = {"name": "javascripted", "description": "is  cool roff", "author": 1}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'javascripted')








         
