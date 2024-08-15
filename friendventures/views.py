from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Friendventure
from .serializers import FriendventureSerializer

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