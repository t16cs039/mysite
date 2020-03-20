from django.shortcuts import render, redirect

from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import PasswordChangeForm

from django.urls import reverse_lazy

from .models import Member

import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_API_KEY


# Create your views here.
class Top(TemplateView):
    template_name = 'authentication/top.html'
    '''
    def post(self, request, *args, **kwargs):
        try:
            charge = stripe.Charge.create(
                amount=4000,
                currency='jpy',
                source=token,
                description='This is a test',
            )
        except stripe.error.CardError as e:
            context = self.get_context_data()
            context['message'] = 'Your payment cannot be completed. The card has been declined.'
            return render(request, 'top.html', context)
        else:
            return redirect('authentication:top')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data_key'] = settings.STRIPE_PUBLIC_KEY
        context['data_amount'] = 4000
        context['data_name'] = 'WITHER'
        context['data_description'] = 'TEST'
        return context
    '''
class Home(LoginRequiredMixin, TemplateView):
    model = Member
    template_name = 'authentication/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member'] = Member.objects.get(user=self.request.user)
        return context

class Login(LoginView):
    template_name = 'authentication/login.html'

class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('authentication:password_change_done')
    template_name = 'authentication/password_change.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member'] = Member.objects.get(user=self.request.user)
        return context

class PasswordChangeDone(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'authentication/password_change_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member'] = Member.objects.get(user=self.request.user)
        return context

class Complete(TemplateView):
    template_name = 'authentication/complete.html'