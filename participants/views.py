from rest_framework import generics, permissions
from fv_api.permissions import IsOwnerOrReadOnly
from .models import Participant
from .serializers import ParticipantSerializer


class ParticipantList(generics.ListCreateAPIView):
    serializer_class = ParticipantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Participant.objects.all()
        friendventure_id = self.request.query_params.get('friendventure', None)
        if friendventure_id:
            queryset = queryset.filter(friendventure_id=friendventure_id)
        return queryset

    def perform_create(self, serializer):
        participant = serializer.save(owner=self.request.user)


class ParticipantDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ParticipantSerializer
    queryset = Participant.objects.all()
