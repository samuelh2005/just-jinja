from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'gaming_cms/index.html')
