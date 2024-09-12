from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from fv_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """
    API View to list all comments or create a new comment.
    Filtering is done using the 'friendventure' field.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['friendventure']

    def perform_create(self, serializer):
        """
        Save the new comment with the current user as the owner.
        """
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API View to retrieve, update, or delete a specific comment.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
