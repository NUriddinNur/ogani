from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    university = 'agrar'
    fakultet = 'dexqonchlik'
    context = {'university': university, 'fakultet': fakultet}
    return render(request, 'index.html', context)