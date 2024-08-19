from django.contrib.auth.models import User
from .models import Participant
from friendventures.models import Friendventure
from rest_framework import status
from rest_framework.test import APITestCase
from django.shortcuts import get_object_or_404

class ParticipantListViewTest(APITestCase):
    def setUp(self):
        self.testuser = User.objects.create_user(
            username="testuser",
            password="password",
        )
        self.testuser2 = User.objects.create_user(
            username="testuser2",
            password="password2",
        )

        self.test_friendventure = Friendventure.objects.create(
            owner=self.testuser, 
            title='friendventure title', 
            date='2024-08-29',
            time='14:00:00'
        )
    
    # due to the signal the first participant is always the owner of the friendventure
    def test_participant_is_created_automatically_with_owner_of_friendventure(self):
        response = self.client.get('/participants/')
        participant_count = Participant.objects.count()
        self.assertEqual(participant_count, 1)

    def test_can_list_participants(self):
        response = self.client.get('/participants/') 
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_participate_in_friendventure(self):
        self.client.login(username='testuser2', password='password2')
        response = self.client.post(
            '/participants/', {
                'friendventure': self.test_friendventure.id,
                }
        )
        count = Participant.objects.count()
        self.assertEqual(count, 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cant_participate(self):
        response = self.client.post(
            '/participants/', {
                'friendventure': self.test_friendventure.id,
                }
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class ParticipantDetailViewTest(APITestCase):
    def setUp(self):
        self.testuser1 = User.objects.create_user(
            username="testuser",
            password="password",
        )
        self.testuser2 = User.objects.create_user(
            username="testuser2",
            password="password2",
        )
        self.test_friendventure1 = Friendventure.objects.create(
            owner= self.testuser1,
            title = 'friendventure title testuser1',
            date = '2024-09-01',
            time ='15:00:00',
            place = 'Test place testuser1',
            description = 'Test description 1',
            category = 'Indoor'
        )
        self.test_friendventure2 = Friendventure.objects.create(
            owner= self.testuser2,
            title = 'friendventure title testuser2',
            date = '2024-09-03',
            time ='09:00:00',
            place = 'Test place testuser2',
            description = 'Test description 2',
        )
        self.test_participation = Participant.objects.create(
            owner= self.testuser1,
            friendventure = self.test_friendventure2,
        )

    def test_can_retrieve_participant_with_id(self):
        participant_id = self.test_participation.id
        response = self.client.get(f'/participants/{participant_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_comment_using_invalid_id(self):
        response = self.client.get('/participants/2018/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_delete_own_participation(self):
        self.client.login(username='testuser2', password='password2')
        response = self.client.delete('/participants/2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # the first participant is testuser1 due to signal that creates automatic
    # participation for owner of friendventure
    def test_user_cant_delete_other_users_participation(self):
        self.client.login(username='testuser2', password='password2')
        response = self.client.delete('/participants/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
