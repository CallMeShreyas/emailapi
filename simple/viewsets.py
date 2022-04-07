from rest_framework import viewsets
from .models import Email
from . import serializers


class EmailViewset(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = serializers.EmailSerializer

