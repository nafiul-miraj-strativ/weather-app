from django.urls import path,include
from .views import MyDistrictView, TemperatureFetch, PmFetch
from .services import AverageTemperature

urlpatterns = [
    path('mydistricts/', MyDistrictView.as_view(), name='Total districts'),
    path('temperature/', TemperatureFetch.as_view(), name='Temperature'),
    path('pm/', PmFetch.as_view(), name='PM'),
    path('average/', AverageTemperature.as_view(), name='Average-Temperature'),
]
