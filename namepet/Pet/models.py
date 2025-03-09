from django.db import models

# Create your models here.
class Adoptee(models.Model):
    name = models.CharField(null = True, max_length=63, blank=True)
    breed = models.CharField(max_length=31)
    age = models.IntegerField()
    photo = models.ImageField(blank = True, null=True, upload_to=None, height_field=None, width_field=None, max_length=255)
    species = models.CharField(max_length=63)

    def __str__(self):
        if self.name:
            return self.species + " - " + self.name + " - " + self.breed
        else:
            return self.species + " - To Be Named" + " - " + self.breed
