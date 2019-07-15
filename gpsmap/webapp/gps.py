
# # getting models to work without manage.py
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gpsmap.settings")
# import django
# django.setup()
# from webapp.models import Address
# ______________________________________________________________________

from geopy.geocoders import Nominatim
import folium
import os
import secrets

def gps_coord(location):
    gs = Nominatim(user_agent='Dima2')
    location = gs.geocode(location, timeout=3)
    if not location:
        return {'fulladdress':"Not found", 'lat':0.000000, 'lon':0.000000}
    else:
        return {'fulladdress':location.address, 'lat':location.latitude, 'lon':location.longitude}
    # str(location.latitude)+" "+str(location.longitude)
    # return [location.address, location.latitude, location.longitude]

class GenerateMap:

    map = folium.Map(location = [48.4680221, 35.0417711], zoom_start = 6,)
    fg = folium.FeatureGroup(name="My Points")

    def add_point(self, loc_dict):
        loc_list = [loc_dict['lat'], loc_dict['lon']]
        info = loc_dict['fulladdress']
        # print('>>>>>>>>>>>>>', info, loc_list)
        self.fg.add_child(folium.Marker(location = loc_list, popup=info, icon=folium.Icon(color='darkblue')))


    def get_html(self):
        hex = secrets.token_hex(4)
        html_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates', 'maps', 'GPS_map_'+hex+'.html')

        self.map.add_child(self.fg)
        # self.map.add_child(folium.LayerControl())
        # if os.path.exists(html_file):
        #     os.remove(html_file)
            # print(">>>>>>>>>>>>>>>>> file removed")
        self.map.save(html_file)
        return html_file
#
# if __name__ == '__main__':
#     gps = gps_coord('Poltava')
#     print ('>>>>>>>>>>>>>', gps )
#     make_map(gps)
