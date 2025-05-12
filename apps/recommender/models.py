from django.db import models

class TravelInput(models.Model):
    current_lat=models.FloatField()
    current_long= models.FloatField()
    destination_district=models.CharField(max_length=100)
    travel_date=models.DateField()
    
    def __str__(self): 
         return self.destination_district
       