from rest_framework import permissions, generics
from .models import Friendventure
from .serializers import FriendventureSerializer
from fv_api.permissions import IsOwnerOrReadOnly
from django.db.models import Count

class FriendventureList(generics.ListCreateAPIView):
    queryset = Friendventure.objects.all()
    serializer_class=FriendventureSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FriendventureDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FriendventureSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Friendventure.objects.annotate(
        bookmarks_count = Count('bookmarks', distinct=True),
        comments_count = Count('comment', distinct=True),
        participants_count = Count('participants', distinct=True)
    ).order_by('-created_at')