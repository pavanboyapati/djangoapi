from rest_framework import generics
from rest_framework import status
from .serializers import ScotersSerializer
from .models import Scoters
import geopy.distance


class ScoterListView(generics.ListCreateAPIView):
    queryset = Scoters.objects.all()

    serializer_class = ScotersSerializer

    # def get_queryset(self):

    #     lat = self.request.GET.get('lat', None)
    #     lng = self.request.GET.get('lng', None)
    #     radius = self.request.GET.get('radius', None)
    #     if self.action == 'filter_shippings':
    #         queryset = queryset.filter(status=2, orderStatus=0)
    #     elif self.action == 'other_action':
    #         queryset = queryset.filter(...)  # other action filter

    #     return queryset


# class ScoterDetailView(generics.ListCreateAPIView):
#     queryset = Scoters.objects.filter(id=id)

#     serializer_class = ScotersSerializer
