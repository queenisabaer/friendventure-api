from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings 


@api_view()
def root_route(request):
    return Response(
        {
            "message": "Welcome to the FriendVenture API. "
            "For further information, please consult the documentation at: "
            "https://github.com/queenisabaer/friendventure-api"
        }
    )


# dj-rest-auth logout view fix
@api_view(['POST'])
def logout_route(request):
    jwt_auth_cookie = settings.REST_AUTH.get('JWT_AUTH_COOKIE')
    jwt_auth_refresh_cookie = settings.REST_AUTH.get('JWT_AUTH_REFRESH_COOKIE')
    jwt_auth_samesite = settings.REST_AUTH.get('JWT_AUTH_SAMESITE')
    jwt_auth_secure = settings.REST_AUTH.get('JWT_AUTH_SECURE')

    response = Response()
    response.set_cookie(
        key=jwt_auth_cookie,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=jwt_auth_samesite,
        secure=jwt_auth_secure,
    )
    response.set_cookie(
        key=jwt_auth_refresh_cookie,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=jwt_auth_samesite,
        secure=jwt_auth_secure,
    )
    return response
