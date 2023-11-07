from django import forms
from django.core.validators import validate_integer

from phonenumbers import is_possible_number, PhoneNumber, SUPPORTED_REGIONS, country_code_for_region

from .models import User

class PhoneField(forms.Field):
    def validate(self, value):
        super().validate(value)

        if value.isdigit():
            for region in SUPPORTED_REGIONS:
                code = country_code_for_region(region)
                if value.startswith(str(code)):
                    break

            number = int(value[len(str(code)):])
            if is_possible_number(PhoneNumber(code, number)):
                return

        raise forms.ValidationError('Incorrect number')


class RegisterForm(forms.ModelForm):
    phone_number = PhoneField(label='Номер телефона')

    class Meta:
        model = User
        fields = ('name', 'surname', 'email', 'phone_number', 'photo', )