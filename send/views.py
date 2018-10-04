from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import permissions

from .serializers import UploadSerializer
from .models import Upload


class UploadView(ModelViewSet):
    # parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UploadSerializer
    queryset = Upload.objects.all()

    def perform_create(self, serializer):
        data = self.request.data
        if 'image_1' not in data:
            raise ValueError('Image not exist')
        else:
            serializer.save()
