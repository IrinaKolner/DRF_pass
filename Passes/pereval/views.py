from rest_framework import generics, viewsets
from .models import Pereval_added
from .serializers import PerevalSerializer, Pereval_addedSerializer


# для проверки всего
class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval_added.objects.all()
    serializer_class = PerevalSerializer


# submitData
class Pereval_addedAPICreate(generics.CreateAPIView):
    queryset = Pereval_added.objects.all()
    serializer_class = Pereval_addedSerializer
