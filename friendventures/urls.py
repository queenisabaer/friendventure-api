from django.urls import path
from friendventures import views

urlpatterns = [
    path(
        "friendventures/",
        views.FriendventureList.as_view(),
        name="friendventure"
    ),
    path(
        "friendventures/<int:pk>/",
        views.FriendventureDetail.as_view(),
        name="friendventure_detail"
    )
]
