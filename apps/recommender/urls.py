from django.urls import path,include

urlpatterns = [
    path('api/v1/recommender/', include(f"apps.recommender.api.v1.urls"),),
]
