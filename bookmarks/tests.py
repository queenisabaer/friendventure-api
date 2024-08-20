from django.contrib.auth.models import User
from .models import Bookmark
from friendventures.models import Friendventure
from rest_framework import status
from rest_framework.test import APITestCase


class BookmarkListViewTest(APITestCase):
    """
     Tests for the BookmarkList view.
    """
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="password",
        )
        self.test_friendventure = Friendventure.objects.create(
            owner=self.user,
            title='friendventure title',
            date='2024-08-29',
            time='14:00:00'
        )

    def test_can_list_bookmarks(self):
        response = self.client.get('/bookmarks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_bookmark_a_friendventure(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(
            '/bookmarks/', {
                'friendventure': self.test_friendventure.id,
                }
        )
        count = Bookmark.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cant_bookmark(self):
        response = self.client.post(
            '/bookmarks/', {
                'friendventure': self.test_friendventure.id,
                }
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_cant_bookmark_a_friendventure_twice(self):
        self.client.login(username='testuser', password='password')
        user = User.objects.get(username='testuser')
        friendventure = Friendventure.objects.get(
            id=self.test_friendventure.id
        )
        response = self.client.post(
            '/bookmarks/', {'owner': user, 'friendventure': friendventure}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class BookmarkDetailViewTest(APITestCase):
    """
     Tests for the BookmarkDetail view.
    """
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
            owner=self.testuser1,
            title='friendventure title testuser1',
            date='2024-09-01',
            time='15:00:00',
            place='Test place testuser1',
            description='Test description 1',
            category='Indoor'
        )
        self.test_friendventure2 = Friendventure.objects.create(
            owner=self.testuser2,
            title='friendventure title testuser2',
            date='2024-09-03',
            time='09:00:00',
            place='Test place testuser2',
            description='Test description 2',
        )
        self.test_bookmark = Bookmark.objects.create(
            owner=self.testuser2,
            friendventure=self.test_friendventure1
        )
        self.test_bookmark2 = Bookmark.objects.create(
            owner=self.testuser1,
            friendventure=self.test_friendventure2
        )

    def test_can_retrieve_bookmark_with_id(self):
        bookmark_id = self.test_bookmark.id
        response = self.client.get(f'/bookmarks/{bookmark_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_bookmark_using_invalid_id(self):
        response = self.client.get('/bookmarks/2018/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_delete_own_bookmark(self):
        self.client.login(username='testuser2', password='password2')
        response = self.client.delete('/bookmarks/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cant_delete_other_users_bookmark(self):
        self.client.login(username='testuser2', password='password2')
        response = self.client.delete('/bookmarks/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
