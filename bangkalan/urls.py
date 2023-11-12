from django.urls import path
from . import views

app_name = 'bangkalan'

urlpatterns = [
    path('', views.index, name='index'),
]
