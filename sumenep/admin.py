from django.contrib import admin
from .models import Sumenep, Profile

class SumenepAdmin(admin.ModelAdmin):
    list_display = ('kota',) 

admin.site.register(Sumenep, SumenepAdmin)
admin.site.register(Profile)