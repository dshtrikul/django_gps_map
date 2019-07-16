from geopy.geocoders import Nominatim
import folium
import os
import secrets

def gps_coord(location):
    gs = Nominatim()
    try:
        location = gs.geocode(location, timeout=5)
    except:
        return gps_coord(location)
    if not location:
        return {'fulladdress':"Not found", 'lat':0.000000, 'lon':0.000000}
    else:
        return {'fulladdress':location.address, 'lat':location.latitude, 'lon':location.longitude}

class GenerateMap:

    def __init__(self):
        map = folium.Map(location = [48.4680221, 35.0417711], zoom_start = 6,)
        fg = folium.FeatureGroup(name="My Points")
        self.map = map
        self.fg = fg

    def add_point(self, loc_dict):
        loc_list = [loc_dict['lat'], loc_dict['lon']]
        info = loc_dict['fulladdress']
        self.fg.add_child(folium.Marker(location = loc_list, popup=info, icon=folium.Icon(color='red')))

    def get_html(self):
        # hex = secrets.token_hex(4)
        # html_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates', 'maps', 'GPS_map_'+hex+'.html')
        html_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates', 'maps', 'GPS_map.html')
        self.map.add_child(self.fg)
        self.map.save(html_file)
        return html_file
