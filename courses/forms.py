from django.forms import ModelForm, TextInput, Textarea, Select, DecimalField
from .models import *
from django.views.generic.edit import ModelFormMixin


# Форма создания курса
class CreateCourse(ModelForm):
    price = DecimalField(max_digits=9, decimal_places=2, label='Цена курса')

    class Meta:
        model = Course
        fields = ('name', 'description', 'category', 'price')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', "rows": '4'}),
            'category':  Select(attrs={'class': 'form-control'}),
            'price': TextInput(attrs={'class': 'form-control'})
        }
