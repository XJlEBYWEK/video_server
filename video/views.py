from rest_framework import views
from rest_framework.permissions import IsAdminUser, AllowAny
from . import models, serializer
from rest_framework import generics


class UploadTrackView(generics.CreateAPIView):
    """ Закачивание трека
    """
    queryset = models.Video.objects.all()
    serializer_class = serializer.VideoSerializer
    permission_classes = [AllowAny]

