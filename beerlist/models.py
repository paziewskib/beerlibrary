from django.db import models
from django.urls import reverse


class Brewery(models.Model):
    brewery_name = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    brewery_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('beerlist:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.brewery_name + ' - ' + self.hometown


class Beer(models.Model):
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    beer_name = models.CharField(max_length=200)
    style = models.CharField(max_length=200)
    abv = models.FloatField(max_length=50)
    plato = models.FloatField(max_length=50)
    expired_date = models.DateTimeField(max_length=50)
    is_in_library = models.BooleanField(default=False)

    def __str__(self):
        return self.beer_name
