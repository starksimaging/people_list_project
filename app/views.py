from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm

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
    return render(request, 'app/person_list.html', {
                                                    'people': people,
                                                    'message': 'This is a message from view.py',
                                         })


def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm()
    return render(request, 'app/add_person.html', {'form': form})