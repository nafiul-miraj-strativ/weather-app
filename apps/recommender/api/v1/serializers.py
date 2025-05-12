from rest_framework import serializers
from apps.recommender.models import TravelInput

class TravelInputSerializer(serializers.ModelSerializer):
     class Meta:
          model = TravelInput
          fields = ['current_lat', 'current_long','destination_district','travel_date']