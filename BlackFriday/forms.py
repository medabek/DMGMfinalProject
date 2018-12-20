from django import forms
from django.contrib.auth import authenticate
from .models import Person


class HomeForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'