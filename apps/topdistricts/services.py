import requests
from apps.topdistricts.constants import TEMPERATURE_DATA

class GetTopDistrict:
    def get_top_districts(lat_long_list):
        temp_list = []
        avg_temp_list=[]
        # for data in TEMPERATURE_DATA:
    
        
        # for district in lat_long_list:
        #     # temp_url = f"https://api.open-meteo.com/v1/forecast?latitude={district.get("lat")}&longitude={district.get("long")}&hourly=temperature_2m"
        #     # temp_response = requests.get(temp_url)
        #     # temp_data = temp_response.json()
        #     # temp_list.append(temp_data)
            
        #     print(temp_list)  
        global_index_list = []
        for avg_temp in TEMPERATURE_DATA:
            times = avg_temp.get("hourly").get("time")
            global_index_list = [i for i, s in enumerate(times) if 'T14' in s]
            break
        for avg_temp in TEMPERATURE_DATA:
            temperatures = avg_temp.get("hourly").get("temperature_2m")
            temperature_list = [temp for i, temp in enumerate(temperatures) if i in global_index_list]
            print("temperature_list===============: ")
            # print(temperature_list)
            print(temperature_list)
            
                    
        print(global_index_list)
        return temp_list