from django import forms
from . import models
from cloudinary.forms import CloudinaryFileField

class CreateAccount(forms.ModelForm):
    avatar = CloudinaryFileField(
        options={
            'crop':'thumb',
            'width':200,
            'height':200,
            'folder':'avatars' 
        }
    )
     class Meta:
         model = models.Profile
         fields = ('email','bio','avatar')
