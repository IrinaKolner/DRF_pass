from rest_framework import generics, viewsets
from .models import Pereval_added
from .serializers import PerevalSerializer


# для проверки всего
class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval_added.objects.all()
    serializer_class = PerevalSerializer
