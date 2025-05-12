import requests
from apps.topdistricts.constants import TEMPERATURE_DATA

class GetTopDistrict:
    def get_top_districts(lat_long_list):
        temp_list = []
        pm_list = []
        average_temp_list=[] 
        average_pm_list=[]
        
        #api of temperature
        for district in lat_long_list:
            temp_url = f"https://api.open-meteo.com/v1/forecast?latitude={district.get("lat")}&longitude={district.get("long")}&hourly=temperature_2m&forecast_days=7"
            temp_response = requests.get(temp_url)
            temp_data = temp_response.json()
            temp_list.append(temp_data)
        #api of pm2_5
        for district in lat_long_list:
            pm_url=f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={district.get("lat")}&longitude={district.get("long")}&hourly=pm2_5&forecast_days=7"
            pm_response= requests.get(pm_url)
            pm_data=pm_response.json()
            pm_list.append(pm_data)
            print(pm_list)
        global_index_list = []
        
        for avg_temp in temp_list:
            times = avg_temp.get("hourly").get("time")
            global_index_list = [i for i, s in enumerate(times) if 'T14' in s]
            break
        for avg_temp in temp_list:
            lat = avg_temp.get("latitude")
            lang = avg_temp.get("longitute")
            temperatures = avg_temp.get("hourly").get("temperature_2m")
            temperature_list = [temp for i, temp in enumerate(temperatures) if i in global_index_list]
            for i in temperature_list:
                average_temp=sum(temperature_list)/len(temperature_list)
            average_temp_list.append({
                'temperature':f"{average_temp:.2f}"
            })
        for avg_pm in pm_list:
            lat = avg_pm.get("latitude")
            lang = avg_pm.get("longitute")
            pms= avg_pm.get("hourly").get("pm2_5")
            pm_list = [pm for i, pm in enumerate(pms) if i in global_index_list]
            for i in pm_list:
                average_pm=sum(pm_list)/len(pm_list)
            average_pm_list.append({
                'pm_2.5':f"{average_pm:.2f}"
            })       
        for i,(d,u) in enumerate(zip(lat_long_list,average_temp_list)):
            d.update(u)
            lat_long_list[i]=d
        
        for i,(d,u) in enumerate(zip(lat_long_list,average_pm_list)):
            d.update(u)
            lat_long_list[i]=d
            
        final_list=sorted(lat_long_list, key=lambda x:(x['temperature'],x['pm_2.5']))
        print(final_list)

        return final_list