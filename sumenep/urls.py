from django.urls import path
from . import views

app_name = 'sumenep'

urlpatterns = [
    path('', views.index, name='index'),
]
