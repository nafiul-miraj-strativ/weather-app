from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from apps.topdistricts.services import GetTopDistrict

class MyDistrictView(APIView):
    def get(self, request):
        url = 'https://raw.githubusercontent.com/strativ-dev/technical-screening-test/main/bd-districts.json'
        response = requests.get(url)
        data = response.json()
        lat_long_list = []
        for district in data.get('districts', []):
            lat_long_list.append({
                'name': district.get('name'),
                'lat': "{:.2f}".format(float(district.get('lat'))),
                'long': "{:.2f}".format(float(district.get('long'))),
            })
        top_coolest_city = GetTopDistrict.get_top_districts(lat_long_list)
               
        return Response(top_coolest_city,status=status.HTTP_201_CREATED)
    
        
        
        