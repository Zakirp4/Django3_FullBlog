from django import forms
from django.forms import ModelForm
from .models import Category, Post


class CategoryAddForm(forms.Form):
     name = forms.CharField()
    # class Meta:
    #     model = Category
    #     widgets = {
    #          'name': forms.TextInput(attrs={'class': 'form-control'}),
    #     }


class AuthorAddForm(forms.Form):
     name = forms.CharField()

class PostAddForm(forms.ModelForm):
     # title = forms.CharField()
     # description = forms.CharField()
    class Meta:
        model = Post
        fields = ['title', 'description', 'author','category','image']


