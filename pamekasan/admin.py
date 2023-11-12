from django.contrib import admin
from .models import Pamekasan, Profile

class PamekasanAdmin(admin.ModelAdmin):
    list_display = ('kota',) 

admin.site.register(Pamekasan, PamekasanAdmin)
admin.site.register(Profile)
