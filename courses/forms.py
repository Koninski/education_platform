from django.forms import ModelForm, TextInput, Textarea, Select
from .models import *


# Форма создания курса
class CreateCourse(ModelForm):

    class Meta:
        model = Course
        fields = ('name', 'description', 'category', 'price')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', "rows": '4'}),
            'category':  Select(attrs={'class': 'form-control'}),
            'price': TextInput(attrs={'class': 'form-control'})
        }
