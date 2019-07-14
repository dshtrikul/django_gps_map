from django.db import models
from geopy.geocoders import Nominatim
import folium
# from gps import get_dummy

class Address(models.Model):

    address = models.TextField()
    gps = models.CharField(max_length=100)
    fulladdress = models.CharField(max_length=300)

    # gps = models.CharField(default=lambda adr=adr:Address.get_gps(address=adr), max_length=100)

    # @classmethod
    # def get_gps(cls, **kwargs):
    #     gs = Nominatim(user_agent='Dima')
    #     address_from_db = Address.objects.get(**kwargs).__str__()
    #     location = gs.geocode(address_from_db)
    #     # return [location.address, location.latitude, location.longitude]
    #     return str(location.latitude)+" "+str(location.longitude)
    #
    #
    # adr = 'Poltava'


    def __str__(self):
        return self.address
