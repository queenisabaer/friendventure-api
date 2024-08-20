from django.urls import path
from participants import views

urlpatterns = [
    path('participants/', views.ParticipantList.as_view()),
    path('participants/<int:pk>/', views.ParticipantDetail.as_view()),
]
