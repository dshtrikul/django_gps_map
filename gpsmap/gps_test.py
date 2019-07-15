
# getting models to work without manage.py
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gpsmap.settings")
import django
django.setup()
from webapp.models import Address
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

def make_map(loc_dict):
    map = folium.Map(location = [48.4680221, 35.0417711], zoom_start = 6,)
    fg = folium.FeatureGroup(name="My Points")

    loc_list = [loc_dict['lat'], loc_dict['lon']]
    print('>>>>>>>>>>>>>', loc_list)
    info = loc_dict['fulladdress']
    fg.add_child(folium.Marker(location = loc_list, popup=info, icon=folium.Icon(color='darkblue')))
    map.add_child(fg)
    map.add_child(folium.LayerControl())
    map.save('Map_My_Test_Map.html')


if __name__ == '__main__':
    gps = gps_coord('Poltava')
    print ('>>>>>>>>>>>>>', gps )
    make_map(gps)
