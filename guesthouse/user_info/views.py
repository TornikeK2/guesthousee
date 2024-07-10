
from rest_framework import  viewsets
from .models import ContactInfo
from .serializers import ContactInfoSerializer


class ContactInfoViewSet(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
