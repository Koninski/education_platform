from django.views.generic import CreateView
from django.shortcuts import redirect

from .forms import RegisterForm
from .models import User

class RegisterView(CreateView):
    model = User
    template_name = 'user/register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        form.save()
        return redirect('lessons_list')
