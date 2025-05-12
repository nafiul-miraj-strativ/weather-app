import requests

district_url = 'https://raw.githubusercontent.com/strativ-dev/technical-screening-test/main/bd-districts.json'

def get_district_coordinates(district_name):
    response = requests.get(district_url)
    data = response.json()
    for district in data.get('districts', []):
        if district['name'].lower() == district_name.lower():
            return district['lat'], district['long']

def get_temperature(district_lat, district_long, travel_date):
    temperature_url = f"https://api.open-meteo.com/v1/forecast?latitude={district_lat}&longitude={district_long}&hourly=temperature_2m&start_date={travel_date}&end_date={travel_date}"
    temperature_response = requests.get(temperature_url)
    temperature_data = temperature_response.json()
    times = temperature_data.get("hourly").get("time")
    index_list = [i for i, s in enumerate(times) if 'T14' in s]
    temperatures = temperature_data.get("hourly").get("temperature_2m")
    final_temperature = [temp for i, temp in enumerate(temperatures) if i in index_list]
    return final_temperature[0]

def get_pm(district_lat, district_long, travel_date):
    pm_url = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={district_lat}&longitude={district_long}&hourly=pm2_5&start_date={travel_date}&end_date={travel_date}"
    pm_response = requests.get(pm_url)
    pm_data = pm_response.json()
    times = pm_data.get("hourly").get("time")
    index_list = [i for i, s in enumerate(times) if 'T14' in s]
    pm_values = pm_data.get("hourly").get("pm2_5")
    final_pm = [pm for i, pm in enumerate(pm_values) if i in index_list]
    return final_pm[0]
