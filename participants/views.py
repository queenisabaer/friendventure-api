from rest_framework import generics, permissions
from fv_api.permissions import IsOwnerOrReadOnly
from .models import Participant
from .serializers import ParticipantSerializer


class ParticipantList(generics.ListCreateAPIView):
    serializer_class = ParticipantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Participant.objects.all()

    def perform_create(self, serializer):
        participant = serializer.save(owner=self.request.user)


class ParticipantDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ParticipantSerializer
    queryset = Participant.objects.all()
