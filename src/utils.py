from geopy.geocoders import Nominatim
import folium


def names_to_geo_points(self, cities: list[str]) -> list[tuple[float, float]]:
    geolocator = Nominatim(user_agent="city_to_coordinates")
    coordinates = []

    for city_name in cities:
        location = geolocator.geocode(city_name)
        if location:
            coordinates.append((location.latitude, location.longitude))
    return coordinates


def plot_addresses_on_map(addresses, map):
    geolocator = Nominatim(user_agent="israshell")

    for address in addresses:
        try:
            location = geolocator.geocode(address)
            if location:
                lat, lon = location.latitude, location.longitude

                folium.Marker([lat, lon], popup=address).add_to(map)
        except Exception as e:
            print(f"Error geocoding address {address}: {e}")
    return map





















