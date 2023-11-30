from django.forms import ModelForm, TextInput, Textarea, Select, NumberInput
from .models import Course, Chapter


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


# Форма создания главы
class CreateChapter(ModelForm):

    class Meta:
        model = Chapter
        fields = ('name', 'order', 'description')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'order': NumberInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', "rows": '4'}),
        }


