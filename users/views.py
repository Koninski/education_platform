from django.views.generic import CreateView, TemplateView, View
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from .forms import RegisterForm
from edu.settings import EMAIL_ADDRES, EMAIL_PASSWORD

class RegisterView(CreateView):
    model = get_user_model()
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('lessons_list')

    def form_valid(self, form):
        ''' Отправляем сообщение для подтверждения почты '''
        RegisterForm.confirm_email(form)

        return redirect('email_confirmation_sent')


class EmailConfirmationView(View):
    ''' Представление для отслеживания перехода по ссылке для подтверждения почты '''

    def get(self, request, user_id_base64, user_email_base64, token):
        try: # Декодируем id и email
            user_id = urlsafe_base64_decode(user_id_base64)
            user_email = urlsafe_base64_decode(user_email_base64).decode('utf-8')
            user = get_user_model().objects.get(pk=user_id)
        except (TypeError, ValueError, get_user_model().DoesNotExist):
            user = None

        # Провверяем токен, сохраняем email пользователя при успехе
        if user is not None and default_token_generator.check_token(user, token):
            user.email = user_email
            user.save()
            login(request, user)
            return redirect('email_confirmation_complete')
        else:
            return redirect('email_confirmation_failed')

class EmailConfirmationFailedView(TemplateView):
    ''' Почта не подтверждена '''
    template_name = 'users/email_confirmation_failed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Электронная почта не подтверждена'
        return context


class EmailConfirmationCompleteView(TemplateView):
    ''' Почта подтверждена '''
    template_name = 'users/email_confirmation_complete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Электронная почта успешно подтверждена'
        return context


class EmailConfirmationSentView(TemplateView):
    ''' Ссылка для подтверждения почты отправлена '''
    template_name = 'users/email_confirmation_sent.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Проверьте электронную почту'
        return context