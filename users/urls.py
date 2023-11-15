from django.urls import path

from .views import RegistrationView, EmailConfirmationView, EmailConfirmationFailedView, \
    EmailConfirmationCompleteView, EmailConfirmationSentView, AuthorizationView


url_patterns = [
    path('registration',
         RegistrationView.as_view(), name='registration'),
    path('email_confirmation/<user_id_base64>/<user_email_base64>/<token>/',
         EmailConfirmationView.as_view(), name='email_confirmation'),
    path('email_confirmation_failed',
         EmailConfirmationFailedView.as_view(), name='email_confirmation_failed'),
    path('email_confirmation_complete',
         EmailConfirmationCompleteView.as_view(), name = 'email_confirmation_complete'),
    path('email_confirmation_sent',
         EmailConfirmationSentView.as_view(), name='email_confirmation_sent'),
    path('authorization',
         AuthorizationView.as_view(), name='authorization')
]