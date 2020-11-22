from django import forms
from . import models

class CreateAccount(forms.ModelForm):
     class Meta:
         model = models.Profile
         fields = ('email','bio','avatar')
