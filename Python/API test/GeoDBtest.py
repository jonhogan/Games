import requests
import json
from keys.keys import geoDBKey

url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"
querystring = {
    "namePrefix": "Washington",
    #"countryIds": "RU",
    #"minPopulation":"1000000",
    "limit":"100"
    }

headers = {
    "X-RapidAPI-Key": geoDBKey,
    "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()

city_data_list = []

for city_info in data["data"]:
    city_data = {
        "id": city_info["id"],
        "name": city_info["name"],
        "country": city_info["country"],
        "countryCode": city_info["countryCode"],
        "latitude": city_info["latitude"],
        "longitude": city_info["longitude"],
        "population": city_info["population"]
    }
    city_data_list.append(city_data)

with open("cities.json", "w", encoding='utf-8') as f:
    json.dump(city_data_list, f, indent=4, ensure_ascii=False)