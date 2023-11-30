from django.urls import path, reverse_lazy
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView, \
    PasswordResetDoneView, PasswordChangeView, PasswordChangeDoneView

from .views import RegistrationView, EmailConfirmationView, EmailConfirmationFailedView, \
    EmailConfirmationCompleteView, EmailConfirmationSentView, AuthorizationView, LogOutUser, \
    CustomPasswordResetView, UserProfileView


url_patterns = [
    path('registration',
         RegistrationView.as_view(), name='registration'),
    path('authorization',
         AuthorizationView.as_view(), name='authorization'),
    path('logout', LogOutUser.as_view(), name='logout'),

    path('profile', 
         UserProfileView.as_view(), name='profile'),
    path('password_change', 
         PasswordChangeView.as_view(template_name='users/password_change_form.html'), 
         name='password_change'),
    path('password_change/done', 
         PasswordChangeDoneView.as_view(template_name='users/password_change_complete.html'), 
         name='password_change_done'),

    path('email_confirmation/<user_id_base64>/<user_email_base64>/<token>/',
         EmailConfirmationView.as_view(), name='email_confirmation'),
    path('email_confirmation/sent',
         EmailConfirmationSentView.as_view(), name='email_confirmation_sent'),
    path('email_confirmation/failed',
         EmailConfirmationFailedView.as_view(), name='email_confirmation_failed'),
    path('email_confirmation/complete',
         EmailConfirmationCompleteView.as_view(), name = 'email_confirmation_complete'),

    path('password_reset/', 
         CustomPasswordResetView.as_view(template_name='users/password_reset_form.html',
                                   success_url=reverse_lazy("password_reset_sent")), 
         name='password_reset'),
    path('password_reset/sent',
         PasswordResetDoneView.as_view(template_name = "users/password_reset_sent.html"),
         name='password_reset_sent'),
    path('password_reset/<uidb64>/<token>/', 
         PasswordResetConfirmView.as_view(template_name="users/password_reset_confirmation.html",
                                          success_url=reverse_lazy("password_reset_complete")), 
         name='password_reset_confirm'),
    path('password_reset/complete/', 
         PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), 
         name='password_reset_complete'),
]
