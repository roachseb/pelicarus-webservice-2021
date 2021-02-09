from django import forms
from django.forms import ModelForm
from .models import Organism,Payment,Campaign,CustomInfo,Action


class OrganismForm(ModelForm):
    class Meta:
        model = Organism