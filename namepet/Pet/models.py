from django.db import models

# Create your models here.
class adoptee(models.Model):
    name = models.CharField(null = True, max_length=63)
    breed = models.CharField(max_length=31)
    age = models.IntegerField()
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=255)
    species = models.CharField(max_length=63)