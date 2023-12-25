import folium
import cities as pf
import geopy
from utils import *

# TODO: insert to config
latitude = 31.0461
longitude = 34.8516
zoom_level = 10


m = folium.Map(location=[latitude, longitude], zoom_start=zoom_level, control_scale=True)
cities_names = ['Ashdod', 'Ashkelon', ' Beer sheva ','Bney brak ', 'Hadera', 'Haifa', 'Herzelia', 'Jerusalem', 'kiryat shmona',' modeen',' Netanya',' Ofakim', 'Rehovot', 'Rishon Lezion', "Sderot", "Tel Aviv"]
cities_geo_points = names_to_geo_points(cities_names)
print(cities_geo_points)

for coords,city in zip(cities_geo_points,cities_names):
    folium.Marker(location=coords, popup=city).add_to(m)



m.save("map.html")

