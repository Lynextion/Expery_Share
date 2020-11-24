from django import forms
from . import models
from cloudinary.forms import CloudinaryFileField

class CreateArticle(forms.ModelForm):
    thumb = CloudinaryFileField(
        options={
            'width':1000,
            'height':1000,
            'folder':'thumbs'
        }
    )
     class Meta:
         model = models.Article
         fields = ('title','body','slug','thumb')
