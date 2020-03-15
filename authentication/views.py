from django.shortcuts import render

from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import PasswordChangeForm

from django.urls import reverse_lazy

from .models import Member

# Create your views here.
class Top(LoginRequiredMixin, TemplateView):
    model = Member
    template_name = 'authentication/top.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member'] = Member.objects.get(user=self.request.user)
        return context

class Login(LoginView):
    template_name = 'authentication/login.html'

class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_change_done')
    template_name = 'authentication/password_change.html'

class PasswordChangeDone(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'authentication/password_change_done.html'