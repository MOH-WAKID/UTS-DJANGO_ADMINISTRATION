from django.shortcuts import render

def index(request):
    return render(request, 'bangkalan/index.html')


# Create your views here.
