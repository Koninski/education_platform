import smtplib
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.tokens import default_token_generator
from django.forms import TextInput, EmailInput, PasswordInput
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse_lazy
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from phonenumbers import is_possible_number, PhoneNumber, SUPPORTED_REGIONS, country_code_for_region
from edu.settings import EMAIL_ADDRESS, EMAIL_PASSWORD


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


class RegistrationForm(UserCreationForm):
    # phone_number = PhoneField(label='Номер телефона')

    def confirm_email(self):
        '''
        Подтверждение почты.
        Отправляет сообщение с ссылкой для подтверждения на указанную почту.
        '''

        # Соединяемся с smtp сервером для отправки сообщения
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.starttls()
        smtpObj.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        # Создаём в бд пользователя с данными формы, но без email
        user = get_user_model().objects.create(username=self.cleaned_data['username'])
        user.set_password(self.cleaned_data['password1'])
        user.save()

        token = default_token_generator.make_token(user) # токен для проверки email'а
        user_id_base64 = urlsafe_base64_encode(force_bytes(user.pk))  # кодируем айди пользователя
        email = self.cleaned_data.pop('email')
        user_email_base64 = urlsafe_base64_encode(force_bytes(email)) # и email для отправки в url
        activation_url = reverse_lazy('email_confirmation',
                                      kwargs={'user_id_base64': user_id_base64,
                                              'user_email_base64': user_email_base64,
                                              'token': token})

        # Отправляем сообщение на почту и заканчиваем сессию smtp сервера
        msg = MIMEMultipart()
        msg['From'] = f'Gits <{EMAIL_ADDRESS}>'
        msg['To'] = email
        msg['Subject'] = 'Complete the regisrtation!'
        msg.attach(MIMEText(f'Confirm your email by following the link: https:/{activation_url}', 'plain', 'utf-8'))
        smtpObj.send_message(msg)
        smtpObj.quit()

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'password1': PasswordInput(attrs={'class': 'form-control'}),
            'password2': PasswordInput(attrs={'class': 'form-control'})
        }
