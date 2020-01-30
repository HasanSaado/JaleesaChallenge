from django import forms
from django.forms import ModelForm

from .models import *


class BabysitterForm(forms.ModelForm):

    class Meta:
        model = Babysitter
        fields = '__all__'