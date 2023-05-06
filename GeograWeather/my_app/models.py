from django.db import models

# Create your models here.
class Continent(models.Model):
    continent_name = models.CharField(max_length=30, unique=True)
    continent_img = models.TextField()

    def __str__(self):
        return str(self.continent_name)

class Country(models.Model):
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE, related_name="country")
    country_name = models.CharField(max_length=30, unique=True)
    flag = models.TextField(blank=True)

    def __str__(self):
        return str(self.country_name)
    
class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="city")
    city_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return str(self.city_name)
    
class DateWeather(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="dateweather")
    date = models.DateField()
    weather_status = models.CharField(max_length=30)
    status_icon = models.TextField(blank=True)
    wind_speed = models.IntegerField()
    humidity = models.IntegerField()
    temperature = models.IntegerField()

    # def __str__(self):
    #     return str(self.city)
