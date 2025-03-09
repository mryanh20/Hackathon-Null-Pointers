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
        return str(self.id) + " - " + self.species + " - " + self.breed + " - " + self.name
    else:
        return str(self.id) + " - " + self.species + " - " + self.breed + " - Unnamed"
        
def createPet(nbreed, nage, nspecies):
    a = Adoptee(breed = nbreed, age = nage, species = nspecies)
    a.save()
        
def createPet(nname, nbreed, nage, nspecies):
    a = Adoptee(name = nname, breed = nbreed, age = nage, species = nspecies)
    a.save()

def setName(self, nname):
    self.name = nname
    self.save()

def setBreed(self, nbreed):
    self.breed = nbreed
    self.save()

def setPhoto(self, nage):
    self.save()

def setSpecies(self, nspecies):
    self.species = nspecies
    self.save()

def getAllData(self, nspecies):
    self.species = nspecies
    self.save()




    