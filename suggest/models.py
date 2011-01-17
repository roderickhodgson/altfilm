from django.db import models

# Create your models here.
#class preferences(models.Model):
#    tag = models.CharField(max_length=50)
class Director(models.Model):
    name = models.CharField(max_length=50)

class Country(models.Model):
    name = models.CharField(max_length=50)

class Venue(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)

    def dist_to(self, pos):
        if self.lat != "":
            lat, lng = pos
            return ((float(lat)-float(self.lat))**2 + (float(lng)-float(self.lng))**2)**0.5
        else:
            return 1000000

class Film(models.Model):
    title = models.CharField(max_length=50)
    country = models.ForeignKey(Country)
    director = models.ForeignKey(Director)
    venues = models.ManyToManyField(Venue)

