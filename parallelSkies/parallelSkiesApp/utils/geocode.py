from opencage.geocoder import OpenCageGeocode
from dotenv import load_dotenv
import os

load_dotenv()

OPENCAGE_API_KEY = os.getenv('OPENCAGE_API_KEY')

def get_coordinates(city_name):
    key = OPENCAGE_API_KEY
    geocoder = OpenCageGeocode(key)
    result = geocoder.geocode(city_name)

    if result and len(result):
        lat = result[0]['geometry']['lat']
        lon = result[0]['geometry']['lng']
        return lat, lon
    else:
        return None, None
