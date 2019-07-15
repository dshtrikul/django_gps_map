from django.db import models

class Address(models.Model):

    address = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=7, null=True, blank=True)
    fulladdress = models.CharField(max_length=300)

    def __str__(self):
        return self.address

class Files(models.Model):

    txtfile = models.FileField(upload_to='txtfiles/', null=True, blank=True)
