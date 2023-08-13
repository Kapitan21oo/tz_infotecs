from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Geoname
from .serializers import GeonameSerializer


class CityDetailView(APIView):
    def get(self, request, geonameid):
        city = Geoname.objects.get(geonameid=geonameid)
        serializer = GeonameSerializer(city)
        return Response(serializer.data)


class CityListView(APIView):
    def get(self, request):
        page = request.query_params.get('page', 1)
        per_page = request.query_params.get('per_page', 10)
        cities = Geoname.objects.all()[(int(page) - 1) * int(per_page):int(page) * int(per_page)]
        serializer = GeonameSerializer(cities, many=True)
        return Response(serializer.data)


class CityComparisonView(APIView):
    def get(self, request):
        city1_name = request.query_params.get('city1')
        city2_name = request.query_params.get('city2')

        city1 = Geoname.objects.filter(name=city1_name).order_by('-population').first()
        city2 = Geoname.objects.filter(name=city2_name).order_by('-population').first()

        if city1.latitude > city2.latitude:
            northern_city = city1
        else:
            northern_city = city2

        same_timezone = city1.timezone == city2.timezone

        response_data = {
            'city1': GeonameSerializer(city1).data,
            'city2': GeonameSerializer(city2).data,
            'northern_city': GeonameSerializer(northern_city).data,
            'same_timezone': same_timezone,
        }

        return Response(response_data)


class CityAutocompleteView(APIView):
    def get(self, request):
        query = request.query_params.get('query')
        matching_cities = Geoname.objects.filter(name__icontains=query).values('name')
        return Response(matching_cities)
