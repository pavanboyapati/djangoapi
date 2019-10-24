from rest_framework import viewsets
from rest_framework import status
from .serializers import ScotersSerializer
from rest_framework.response import Response
from .models import Scoters
import geopy.distance
import json
import collections


class ScoterListView(viewsets.ModelViewSet):
    queryset = Scoters.objects.all()

    serializer_class = ScotersSerializer

    def list(self, request):
        lat = self.request.GET.get('lat', None)
        lng = self.request.GET.get('lng', None)
        radius = self.request.GET.get('radius', None)
        queryset = Scoters.objects.filter(is_reserved=False)
        serializer = ScotersSerializer(queryset, many=True)
        if (lat is None or lng is None or radius is None):
            return Response(serializer.data)
        return Response(self.filter_if_not_within_radius(serializer.data, lat, lng, radius))

    def filter_if_not_within_radius(self, data, lat, lng, radius):

        scoters = json.loads(json.dumps(data))
        filtered_scoters = []
        for scoter in scoters:
            # print(scoter['lat'])
            distance_m = geopy.distance.vincenty(
                (lat, lng), (scoter['lat'], scoter['lng'])).meters
            if(distance_m <= float(radius)):
                filtered_scoters.append(collections.OrderedDict(scoter))

        return filtered_scoters  # json.dumps(filtered_scoters)
