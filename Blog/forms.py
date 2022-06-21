from pyexpat import model
from statistics import mode
from attr import attrs, fields
from django import forms
from django.forms import ModelForm
from matplotlib import widgets
from .models import *
from django import forms
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            # 'fetured_image' : forms.TextInput(attrs= {'class':'text-input'}),
            'title': forms.TextInput(attrs= {'class':'text-inputckeditor'}),
            'author':forms.TextInput(attrs= {'class':'text-inputckeditor'}),
            'category':forms.Select(attrs= {'class':'text-inputckeditor'}),
            # 'content':,
            'slug':forms.TextInput(attrs= {'class':'text-inputckeditor'}),
            'status':forms.Select(attrs= {'class':'text-inputckeditor'}),
            'section':forms.Select(attrs= {'class':'text-inputckeditor'}),
            

        }
class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs= {'class':'text-inputckeditor'}),
            'description': forms.Textarea(attrs= {'class':'text-inputckeditor'}),
        }