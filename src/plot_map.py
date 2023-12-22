import folium
import city_analysis as pf


# TODO: insert to config
latitude = 31.0461
longitude = 34.8516
zoom_level = 10


m = folium.Map(location=[latitude, longitude], zoom_start=zoom_level, control_scale=True)
cities_names = ['Ashdod', 'Ashkelon', ' Beer sheva ','Bney brak ', 'Hadera', 'Haifa', 'Herzelia', 'Jerusalem', 'kiryat shmona',' modeen',' Netanya',' Ofakim', 'Rehovot', 'Rishon Lezion', "Sderot", "Tel Aviv"]

#cities_points = pf.city_name_to_points(cities_names)

#m.save("map.html")

