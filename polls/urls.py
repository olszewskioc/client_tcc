from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("stream", views.stream, name="stream"),
    path("video-stream", views.video_stream, name="video-stream"),
]