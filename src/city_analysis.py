from geopy.geocoders import Nominatim
import folium


class City:

    @staticmethod
    def city_name_to_points(self, cities: list[str]) -> list[tuple[float, float]]:
        geolocator = Nominatim(user_agent="city_to_coordinates")
        coordinates = []

        for city_name in cities:
            location = geolocator.geocode(city_name)
            if location:
                coordinates.append((location.latitude, location.longitude))

        return coordinates


