from django.contrib.auth.models import User
from .models import Comment
from friendventures.models import Friendventure
from rest_framework import status
from rest_framework.test import APITestCase

class CommentListViewTest(APITestCase):
    """
     Tests for the CommentList view.
    """
    def setUp(self):
        self.testuser = User.objects.create_user(
            username="testuser",
            password="password",
        )
        self.test_friendventure = Friendventure.objects.create(
            owner=self.testuser, 
            title='friendventure title', 
            date='2024-08-29',
            time='14:00:00'
        )

    def test_can_list_comments(self):
        Comment.objects.create(
            owner=self.testuser, 
            friendventure=self.test_friendventure, 
            content="A test comment"
        )
        response = self.client.get('/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_logged_in_user_can_create_comment(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(
            '/comments/', {
                'friendventure': self.test_friendventure.id,
                'content': 'A test comment',
                }
        )
        count = Comment.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cant_create_comment(self):
        response = self.client.post(
            '/comments/', {
                'comment': 'friendventure title',
                }
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class CommentDetailViewTest(APITestCase):
    """
     Tests for the CommentDetail view.
    """
    def setUp(self):
        testuser1 = User.objects.create_user(
            username="testuser1",
            password="password1",
        )
        testuser2 = User.objects.create_user(
            username="testuser2",
            password="password2",
        )
        test_friendventure1 = Friendventure.objects.create(
            owner= testuser1,
            title = 'friendventure title testuser1',
            date = '2024-09-01',
            time ='15:00:00',
            place = 'Test place testuser1',
            description = 'Test description 1',
            category = 'Indoor'
        )
        test_friendventure2 = Friendventure.objects.create(
            owner= testuser2,
            title = 'friendventure title testuser2',
            date = '2024-09-03',
            time ='09:00:00',
            place = 'Test place testuser2',
            description = 'Test description 2',
        )
        test_comment1 = Comment.objects.create(
            owner= testuser1,
            friendventure = test_friendventure2,
            content = 'Nice friendventure testuser 2'
        )
        test_comment2 = Comment.objects.create(
            owner= testuser2,
            friendventure = test_friendventure1,
            content = 'Good friendventure testuser 1'
        )

    def test_can_retrieve_comment_with_id(self):
        response = self.client.get('/comments/1/')
        self.assertEqual(response.data['content'], 'Nice friendventure testuser 2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_comment_using_invalid_id(self):
        response = self.client.get('/comments/2018/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_comment(self):
        self.client.login(username='testuser1', password='password1')
        response = self.client.put('/comments/1/', {
                'content': 'Really nice friendventure testuser 2',
                })
        comment = Comment.objects.filter(pk=1).first()
        self.assertEqual(comment.content, 'Really nice friendventure testuser 2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_other_users_comment(self):
        self.client.login(username='testuser1', password='password1')
        response = self.client.put('/comments/2/', {
            'content': 'Friendventure looks bad testuser 1',
            })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_own_comment(self):
        self.client.login(username='testuser1', password='password1')
        response = self.client.delete('/comments/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cant_delete_other_users_comment(self):
        self.client.login(username='testuser1', password='password1')
        response = self.client.delete('/comments/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)