from django.shortcuts import render

def index(request):
    return render(request, 'pamekasan/index.html')


# Create your views here.
