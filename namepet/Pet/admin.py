from django.contrib import admin
from Pet.models import Adoptee


class AdopteeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Adoptee, AdopteeAdmin)