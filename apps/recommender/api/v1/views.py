from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from apps.recommender.services import get_district_coordinates, get_temperature, get_pm
from apps.recommender.api.v1.serializers import TravelInputSerializer

class MyRecommenderVIew(APIView):
    def post(self, request):
        serializer = TravelInputSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        current_lat = data['current_lat']
        current_long = data['current_long']
        destination_district = data['destination_district']
        travel_date = data['travel_date']

        destination_coords = get_district_coordinates(destination_district)
        destination_lat, destination_long = destination_coords

        current_temperature = get_temperature(current_lat, current_long, travel_date)
        destination_temperature = get_temperature(destination_lat, destination_long, travel_date)

        current_pm = get_pm(current_lat, current_long, travel_date)
        destination_pm = get_pm(destination_lat, destination_long, travel_date)

        temperature_difference = destination_temperature - current_temperature
        
        recommendation = {}

        if destination_temperature < current_temperature and destination_pm < current_pm:
            recommendation['status'] = 'Recommended'
            recommendation['message'] = f"Your destination is {abs(temperature_difference):.1f}°C cooler and has significantly better air quality. Enjoy your trip!"
        elif destination_temperature > current_temperature and destination_pm > current_pm:
            recommendation['status'] = 'Not Recommended'
            recommendation['message'] = f"Your destination is {abs(temperature_difference):.1f}°C hotter and has worse air quality than your current location. It's better to stay where you are."
        elif destination_temperature > current_temperature and destination_pm < current_pm:
            recommendation['status'] = 'Not Recommended'
            recommendation['message'] = f"Your destination is {abs(temperature_difference):.1f}°C hotter but has better air quality than your current location. It's better to stay where you are."
        elif destination_temperature < current_temperature and destination_pm > current_pm:
            recommendation['status'] = 'Not Recommended'
            recommendation['message'] = f"Your destination is {abs(temperature_difference):.1f}°C cooler but has worse air quality than your current location. It's better to stay where you are."
        else:
            recommendation['status'] = 'Neutral'
            recommendation['message'] = "Conditions are similar; consider other factors."

        return Response(recommendation, status=status.HTTP_200_OK)
