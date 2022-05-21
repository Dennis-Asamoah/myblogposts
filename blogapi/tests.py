from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase 
from baseapp.models import User, Post


class TESTAPI(APITestCase):
    @classmethod
    def setUpTestData(self):
        user1 = User(username='obide', email='2@gmailk.com', password='123456')
        user1.save()
        post1 = Post(name='Redux', description='contains boilerpaltes', author=user1)
        post1.save() 
        self.url = reverse('posts')
        

    def test_get(self):
        response = self.client.get(self.url, format='json')
        #print (response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  #testing empty test_database
    

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

    def test_post_error(self):
        post = {'description':'nothin was provided in the name field'} 
        response = self.client.post (self.url, post )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
                

    def test_get_item(self):
        # user1 = User(username='Dennis', email='obide1@gmail.com', password='123456')
        # user1.save()
        # post1 = Post(name='DRF is great', description='for creating apis', author=user1)
        # post1.save()
        url = reverse('detailed_view', args=[1])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)    

    def test_delete(self):
        user1 = User(username='oboo', email='obide2@yahoo.com', password='1234567892')
        user1.save()
        post = Post(name="javascript", description="is  cool", author=user1)
        post.save()
        url = reverse('detailed_view', args=[2])
        print(url)
        response = self.client.delete(url)
        self.assertEqual(response.data, 'post was deleted succesfully')

    def test_update(self):
        user1 = User(username='oboo', email='obide2@yahoo.com', password='1234567892')
        user1.save()
        post = Post(name="javascript", description="is  cool", author=user1)
        post.save()
        url = reverse('detailed_view', args=[2])
        print(url)
        data = {"name": "javascripted", "description": "is  cool roff", "author": 1}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'javascripted')

    def test_update_error(self):
        user = User(username='kelvin', email='l@gmail.com', password='569')
        user.save()
        post = Post(name='flutter', author=user)
        post.save()
        url = reverse('detailed_view', args=[2]) 
        post_update = {'name':'', 'description':'name not provided'}
        response = self.client.put(url, post_update)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)








         
