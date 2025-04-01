from django.shortcuts import render
from .models import Person

# Create your views here.

def my_view(request):
    return render(request, 'app/myview.html')



def about_view(request):
    return render(request, 'app/about.html')


def location_view(request):
    return render(request, 'app/location.html')

def welcome_view(request):
    return render(request, 'app/welcome.html')


def person_list(request):
    people = Person.objects.all()
    return render(request, 'app/person_list.html', {'people': people})