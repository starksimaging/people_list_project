from django import forms
from .models import Person, Car


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'age', 'email']




class carForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['manufacturer', 'model', 'year']