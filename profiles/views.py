from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Profile
from .serializers import ProfileSerializer
from fv_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.annotate(
        friendventures_count=Count('owner__friendventure', distinct=True),
        followers_count=Count('owner__followed_by', distinct=True),
        following_count=Count('owner__following', distinct=True),
        participants_count=Count('owner__participant', distinct=True),
        bookmarks_count=Count('owner__bookmark', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer

    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed_by__owner__profile',
    ]

    ordering_fields = [
        'friendventures_count',
        'followers_count',
        'following_count',
        'participants_count',
        'bookmarks_count',
        'owner__following__created_at',
        'owner__followed_by__created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        friendventures_count=Count('owner__friendventure', distinct=True),
        followers_count=Count('owner__followed_by', distinct=True),
        following_count=Count('owner__following', distinct=True),
        participants_count=Count('owner__participant', distinct=True),
        bookmarks_count=Count('owner__bookmark', distinct=True)
    ).order_by('-created_at')
