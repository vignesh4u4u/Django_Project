from geopy.geocoders import Nominatim
from geopy.distance import geodesic
geolocator = Nominatim(user_agent="distance_calculator")

def get_coordinates(city_name):
    location = geolocator.geocode(city_name)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None


city1 = input("Enter the first city (e.g., Chennai): ")
city2 = input("Enter the second city (e.g., Madurai): ")


location1 = get_coordinates(city1)
location2 = get_coordinates(city2)

if location1 and location2:
    distance = geodesic(location1, location2).kilometers
    print(f"The distance between {city1} and {city2} is: {distance:.2f} km")
else:
    print("Could not find the location(s). Please try again.")
