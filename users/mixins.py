from django.shortcuts import redirect

import smtplib
from email.mime.multipart import MIMEMultipart

from edu.settings import EMAIL_ADDRESS, EMAIL_PASSWORD


class EmailMixin():
    def send_message(self, message: MIMEMultipart, subject: str) -> None:
        ''' Метод для отправки сообщения на почту '''

        email = self.cleaned_data['email']

        # Соединяемся с smtp сервером для отправки сообщения
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.starttls()
        smtpObj.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        # Задаём параметры сообщения, чтобы оно было красивым и не улетело в спам
        message['From'] = f'Gits <{EMAIL_ADDRESS}>'
        message['To'] = email
        message['Subject'] = subject

        # Отправляем сообщение и завершаем сессию
        smtpObj.send_message(message, EMAIL_ADDRESS, email)
        smtpObj.quit()


class UserPermissionDeniedMixin():
    ''' Запрещает посещать личный профиль пользователя (для редактирования) '''

    def get(self, request, *args, **kwargs):
        if request.user.username != self.kwargs['username']:
            return redirect('home')
        return super().get(request, *args, **kwargs)