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
                'lat': district.get('lat'),
                'long': district.get('long'),
                'hourly_temperature': [],
            })
        top_coolest_city = GetTopDistrict.get_top_districts(lat_long_list)
               
        return Response(top_coolest_city,status=status.HTTP_201_CREATED)
    
        
# class TemperatureFetch(APIView, MyDistrictView):
#       def get(self,request):
#         temp_url = f"https://api.open-meteo.com/v1/forecast?latitude={MyDistrictView.get()}&longitude=13.41&hourly=temperature_2m"
#         temp_response = requests.get(temp_url)
#         temp_data = temp_response.json()
#         hourly_data = temp_data.get("hourly", {})
#         times = hourly_data.get("time", [])
#         temperatures = hourly_data.get("temperature_2m", [])
#         return Response({
#             "times": times,
#             "temperatures": temperatures
#         }, status=status.HTTP_201_CREATED)
        
# class PmFetch(APIView):
#     def get(self,request):
#         pm_url = "https://air-quality-api.open-meteo.com/v1/air-quality?latitude=52.52&longitude=13.41&hourly=pm2_5"
#         pm_response=requests.get(pm_url)
#         pm_data=pm_response.json()
#         hourly_data = pm_data.get("hourly",{})
#         times = hourly_data.get("time",[])
#         pms = hourly_data.get("pm2_5",[])
#         return Response({
#             "times":times,
#             "pms":pms
#         }, status=status.HTTP_201_CREATED)
        
        
        