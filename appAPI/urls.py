from django.urls import path
from appAPI import views

urlpatterns = [
    path('hello-view/',views.HelloAPIView.as_view()),
]
