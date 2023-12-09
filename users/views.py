from django.views.generic import CreateView, TemplateView, View, UpdateView, DetailView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.contrib.auth.forms import AuthenticationForm
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

from .forms import RegistrationForm, ResetPasswordForm, LinkEmailForm
from .mixins import UserPermissionDeniedMixin


class AuthorizationView(LoginView):
    ''' Авторизация пользователя '''
    form_class = AuthenticationForm
    template_name = 'users/authorization.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context


class RegistrationView(CreateView):
    ''' Регистрация пользователя '''
    model = get_user_model()
    template_name = 'users/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context
    

class CustomPasswordResetView(PasswordResetView):
    ''' Сброс пароля по прикреплённой электронной почте '''
    form_class = ResetPasswordForm

    def form_valid(self, form):
        form.send_reset_link()
        return redirect('password_reset_sent')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Сброс пароля'
        return context


class EmailConfirmationView(View):
    ''' Представление для отслеживания перехода по ссылке для подтверждения почты '''

    def get(self, request, user_id_base64, user_email_base64, token):
        try: # Декодируем id и email
            user_id = urlsafe_base64_decode(user_id_base64)
            user_email = urlsafe_base64_decode(user_email_base64).decode('utf-8')
            user = get_user_model().objects.get(pk=user_id)
        except (TypeError, ValueError, get_user_model().DoesNotExist):
            user = None

        # Проверяем токен, сохраняем email пользователя при успехе
        if user is not None and default_token_generator.check_token(user, token):
            user.email = user_email
            user.save()
            # login(request, user)
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


class UserProfileEditView(UserPermissionDeniedMixin, UpdateView):
    ''' Личный профиль пользвателя с возможностью редактирования '''
    template_name = 'users/edit_profile.html'
    model = get_user_model()
    slug_url_kwarg = 'username'
    fields = ('photo', 'username', 'first_name', 'last_name')

    def get_object(self, queryset=None):
        return get_user_model().objects.get(username=self.kwargs['username'])
    
    def get_success_url(self):
        return reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Личный профиль'
        return context


class LinkEmailView(UserPermissionDeniedMixin, UpdateView):
    ''' Привязка почты к аккаунту '''
    template_name = 'users/link_email.html'
    slug_url_kwarg = 'username'
    model = get_user_model()
    form_class = LinkEmailForm
    
    def form_valid(self, form):
        form.confirm_email(self.kwargs['username'])

        return redirect('email_confirmation_sent')

    def get_object(self, queryset=None):
        return get_user_model().objects.get(username=self.kwargs['username'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Привязка почты'
        return context


class UserProfileView(DetailView):
    ''' Профиль другого пользователя, без возможности редактирования '''
    template_name = 'users/profile.html'
    slug_url_kwarg = 'username'
    context_object_name = 'user'
    model = get_user_model()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['user'].username
        return context
    
    def get_object(self, queryset=None):
        return get_user_model().objects.get(username=self.kwargs['username'])


class LogOutUser(LogoutView):
    next_page = reverse_lazy('home')
