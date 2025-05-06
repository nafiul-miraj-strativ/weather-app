from django.urls import path,include

urlpatterns = [
    path('api/v1/topdistricts/', include(f"apps.topdistricts.api.v1.urls"),),
    # path('temperature/', TemperatureFetch.as_view(), name='Temperature'),
    # path('pm/', PmFetch.as_view(), name='PM'),
    # path('average/', AverageTemperature.as_view(), name='Average-Temperature'),
]
