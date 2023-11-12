from django.shortcuts import render

def index(request):
    return render(request, 'sampang/index.html')


# Create your views here.
