from django import forms
from .models import Target

class Form(forms.Form):
    target = forms.ModelChoiceField(Target.objects.all())
