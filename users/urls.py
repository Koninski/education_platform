from django.urls import path

from .views import RegisterView, EmailConfirmationView, EmailConfirmationFailedView, EmailConfirmationCompleteView, EmailConfirmationSentView

url_patterns = [
    path('register',
         RegisterView.as_view(), name='register'),
    path('email_confirmation/<user_id_base64>/<user_email_base64>/<token>/',
         EmailConfirmationView.as_view(), name='email_confirmation'),
    path('email_confirmation_failed',
         EmailConfirmationFailedView.as_view(), name='email_confirmation_failed'),
    path('email_confirmation_complete',
         EmailConfirmationCompleteView.as_view(), name = 'email_confirmation_complete'),
    path('email_confirmation_sent',
         EmailConfirmationSentView.as_view(), name='email_confirmation_sent')
]