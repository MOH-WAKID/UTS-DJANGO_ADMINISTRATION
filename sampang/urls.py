from django.urls import path
from . import views

app_name = 'sampang'

urlpatterns = [
    path('', views.index, name='index'),
]
