from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from core.models import Person

# Function Based Views

def home(request):
    persons = Person.objects.all()
    # return HttpResponse(Person.objects.all())
    return render(request, 'home.html', {'persons': persons })

def testing(request, id):
    # database query

    return HttpResponse(f"testing {id}")

# Class Based View

class Another(View):
    def get(self, request):
        return HttpResponse("Another one from CBV")
        
