from django import forms
from django.core.validators import validate_integer
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import login
from django.utils.encoding import force_bytes

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from phonenumbers import is_possible_number, PhoneNumber, SUPPORTED_REGIONS, country_code_for_region


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


class RegisterForm(UserCreationForm):
    phone_number = PhoneField(label='Номер телефона')

    @staticmethod
    def confirm_email(form):
        '''
        Подтверждение почты.
        Отправляет сообщение с ссылкой для подтверждения на указанную почту.
        '''

        # Соединяемся с smtp сервером для отправки сообщения
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.starttls()
        smtpObj.login(EMAIL_ADDRES, EMAIL_PASSWORD)

        # Создаём в бд пользователя с данными формы, но без email
        email = form.cleaned_data.pop('email')
        user = get_user_model().objects.create(
            **{key: form.cleaned_data[value] for key, value in zip(
                ('username', 'password', 'phone_number'),
                ('username', 'password1', 'phone_number')
            )}
        )

        token = default_token_generator.make_token(user) # токен для проверки email'а
        user_id_base64 = urlsafe_base64_encode(force_bytes(user.pk))  # кодируем айди пользователя
        user_email_base64 = urlsafe_base64_encode(force_bytes(email)) # и email для отправки в url
        activation_url = reverse_lazy('email_confirmation',
                                      kwargs={'user_id_base64': user_id_base64,
                                              'user_email_base64': user_email_base64,
                                              'token': token})

        # Отправляем сообщение на почту и заканчиваем сессию smtp сервера
        msg = MIMEMultipart()
        msg['From'] = f'Gits <{EMAIL_ADDRES}>'
        msg['To'] = email
        msg['Subject'] = 'Complete the regisrtation!'
        msg.attach(MIMEText(f'Confirm your email by following the link: https:/{activation_url}', 'plain', 'utf-8'))
        smtpObj.send_message(msg)
        smtpObj.quit()


    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')