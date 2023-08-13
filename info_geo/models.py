from django.db import models


class Geoname(models.Model):
    geonameid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    asciiname = models.CharField(max_length=200)
    alternatenames = models.CharField(max_length=10000, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    featureclass = models.CharField(max_length=1)
    featurecode = models.CharField(max_length=10)
    countrycode = models.CharField(max_length=2)
    population = models.IntegerField()
    elevation = models.IntegerField()
    dem = models.IntegerField()
    timezone = models.CharField(max_length=40)
    modification_date = models.DateField()

    def __str__(self):
        return self.name
