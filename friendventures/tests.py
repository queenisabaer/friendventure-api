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

    def test_logged_out_user_cant_create_post(self):
        response = self.client.post(
            '/friendventures/', {
                'title': 'friendventure title',
                }
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class FriendventureDetailViewTest(APITestCase):
    def setUp(self):
        testuser1 = User.objects.create_user(
            username="testuser1",
            password="password1",
        )
        testuser2 = User.objects.create_user(
            username="testuser2",
            password="password2",
        )
        Friendventure.objects.create(
            owner= testuser1,
            title = 'friendventure title testuser1',
            date = '2024-09-01',
            time ='15:00:00',
            place = 'Test place testuser1',
            description = 'Test description 1',
            category = 'Indoor'
        )
        Friendventure.objects.create(
            owner= testuser2,
            title = 'friendventure title testuser2',
            date = '2024-09-03',
            time ='09:00:00',
            place = 'Test place testuser2',
            description = 'Test description 2',
        )

    def test_can_retrive_friendventure_with_id(self):
        response = self.client.get('/friendventures/1/')
        self.assertEqual(response.data['title'], 'friendventure title testuser1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_friendventure_using_invalid_id(self):
        response = self.client.get('/friendventures/2018/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_friendventure(self):
        self.client.login(username='testuser1', password='password1')
        response = self.client.put('/friendventures/1/', {
                'title': 'friendventure update title',
                'date': '2024-09-01',
                'time': '15:00:00',
                'place': 'Test place testuser1',
                })
        friendventure = Friendventure.objects.filter(pk=1).first()
        self.assertEqual(friendventure.title, 'friendventure update title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_other_users_friendventure(self):
        self.client.login(username='testuser1', password='password1')
        response = self.client.put('/friendventures/2/', {
            'title': 'friendventure update title 2',
            'date': '2024-09-03',
            'time':'09:00:00',
            'place': 'Test place testuser2',
            })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_own_friendventure(self):
        self.client.login(username='testuser1', password='password1')
        response = self.client.delete('/friendventures/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cant_delete_other_users_friendventure(self):
        self.client.login(username='testuser1', password='password1')
        response = self.client.delete('/friendventures/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_default_category_is_outdoor(self):
        response = self.client.get('/friendventures/2/')
        self.assertEqual(response.data['category'], 'Outdoor')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    