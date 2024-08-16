from django.contrib.auth.models import User
from .models import Friendventure
from rest_framework import status
from rest_framework.test import APITestCase


class FriendventureListViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="password",
        )

    def test_can_list_friendventures(self):
        testuser = User.objects.get(username='testuser')
        Friendventure.objects.create(
            owner=testuser, 
            title='friendventure title', 
            date='2024-08-29',
            time='14:00:00'
        )
        response = self.client.get('/friendventures/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_friendventure(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(
            '/friendventures/', {
                'title': 'friendventure title',
                'date': '2024-08-29',
                'time':'14:00:00',
                'place': 'Test place',
                'image' : '',
                'description': 'Test description',
                'category': 'Outdoor'
                }
        )
        count = Friendventure.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
