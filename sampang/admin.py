from django.contrib import admin
from .models import Sampang, Profile

class SampangAdmin(admin.ModelAdmin):
    list_display = ('kota',) 

admin.site.register(Sampang, SampangAdmin)
admin.site.register(Profile)