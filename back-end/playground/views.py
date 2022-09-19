from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# request handler 
# request > response ;-)

def hemlo(request):
    # Pull data, transform data, perform actions.. etc..
    return render(request, 'index.html', {'name': 'Teo'})