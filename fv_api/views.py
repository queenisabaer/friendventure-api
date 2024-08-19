from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def root_route(request):
    return Response(
        {
            "message": "Welcome to the FriendVenture API. "
            "For further information, please consult the documentation at: "
            "https://github.com/queenisabaer/friendventure-api"
        }
    )
