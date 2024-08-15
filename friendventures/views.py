from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Friendventure
from .serializers import FriendventureSerializer
from fv_api.permissions import IsOwnerOrReadOnly

class FriendventureList(APIView):
    serializer_class=FriendventureSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    def get(self, request):
        post = Friendventure.objects.all()
        serializer = FriendventureSerializer(post, many= True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = FriendventureSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

class FriendventureDetail(APIView):
    serializer_class = FriendventureSerializer
    permission_classes = [IsOwnerOrReadOnly]
    def get_object(self, pk):
        try:
            friendventure = Friendventure.objects.get(pk=pk)
            self.check_object_permissions(self.request, friendventure)
            return friendventure
        except Friendventure.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        friendventure = self.get_object(pk)
        serializer = FriendventureSerializer(
            friendventure, context={'request': request}
            )
        return Response(serializer.data)

    def put(self, request, pk):
        friendventure = self.get_object(pk)
        serializer = FriendventureSerializer(
            friendventure, data=request.data, context={'request': request}
            )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        friendventure = self.get_object(pk)
        friendventure.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )