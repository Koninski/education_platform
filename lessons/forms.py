from django.forms import ModelForm, TextInput, Textarea, Select, NumberInput
from .models import Lesson


# Форма создания урока
class CreateLesson(ModelForm):

    class Meta:
        model = Lesson
        fields = ('name', 'description')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', "rows": '4'}),
        }
