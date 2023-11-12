from django.contrib import admin
from .models import Bangkalan, Profile

class BangkalanAdmin(admin.ModelAdmin):
    list_display = ('kota',)

admin.site.register(Bangkalan, BangkalanAdmin)
admin.site.register(Profile)
