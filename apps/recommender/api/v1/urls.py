from django.urls import path,include

from apps.recommender.api.v1.views import MyRecommenderVIew

urlpatterns = [
    path('', MyRecommenderVIew.as_view(), name='Recommended'),
    # path('temperature/', TemperatureFetch.as_view(), name='Temperature'),
    # path('pm/', PmFetch.as_view(), name='PM'),
    # path('average/', AverageTemperature.as_view(), name='Average-Temperature'),
]