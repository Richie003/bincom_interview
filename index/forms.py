from django import forms
from .models import *

class Announced_pu_results_form(forms.ModelForm):
    class Meta:
        model = Announced_pu_results
        fields = "__all__"