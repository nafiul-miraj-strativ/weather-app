from .views import MyDistrictView, TemperatureFetch, PmFetch

class AverageTemperature(MyDistrictView,TemperatureFetch):
    def avg_temp(y):
        return 