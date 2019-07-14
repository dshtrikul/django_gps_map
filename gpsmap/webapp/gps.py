#
# # getting models to work without manage.py
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gpsmap.settings")
# import django
# django.setup()
# from webapp.models import Address
# ______________________________________________________________________

from geopy.geocoders import Nominatim
import folium

def gps_coord(location):
    gs = Nominatim(user_agent='Dima')
    location = gs.geocode(location)
    if not location:
        return {'fulladdress':"Not found", 'lat':0.000000, 'lon':0.000000}
    else:
        return {'fulladdress':location.address, 'lat':location.latitude, 'lon':location.longitude}
    # str(location.latitude)+" "+str(location.longitude)
    # return [location.address, location.latitude, location.longitude]

# def gps_full_address(location):
#     gs = Nominatim(user_agent='Dima')
#     location = gs.geocode(location)
#     if not location:
#         return 'Not found'
#     else:
#         return str(location.address)

#
# if __name__ == '__main__':
#     print(get_gps(Address, address='Poltava'))
