from django.urls import path,include

from apps.topdistricts.api.v1.views import MyDistrictView

urlpatterns = [
    path('', MyDistrictView.as_view(), name='Total districts'),
    # path('temperature/', TemperatureFetch.as_view(), name='Temperature'),
    # path('pm/', PmFetch.as_view(), name='PM'),
    # path('average/', AverageTemperature.as_view(), name='Average-Temperature'),
]