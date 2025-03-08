from django.apps import AppConfig
from models import adoptee


class PetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Pet'

def giveName(newName, adoptee):
    adoptee.name = newName 

def updateAge(adoptee):
    adoptee.age += 1