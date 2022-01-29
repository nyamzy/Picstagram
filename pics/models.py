from django.db import models

# Create your models here.
class Location(models.Model):
    place = models.CharField(max_length = 30)


class Category(models.Model):
    category = models.CharField(max_length = 20)


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 100)
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey(Category)
    post_date = models.DateTimeField(auto_now_add = True)
    url = models.URLField(max_length = 200)