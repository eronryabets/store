from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from common.views import TitleMixin
from users.forms import UserLoginForm, UserProfileForm, UserRegisterForm
from users.models import EmailVerification, User


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Store - authorization'


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Congratulations! You have successfully registered.'
    title = 'Store - registration'


class UserProfileView(TitleMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Store - Profile'

    def test_func(self):
        return self.request.user.id == self.kwargs.get("pk")

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))


class EmailVerificationView(TitleMixin, TemplateView):
    title = 'Store - Email verification'
    template_name = 'users/email_verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs.get('code')
        user = User.objects.get(email=kwargs.get('email'))
        email_verification = EmailVerification.objects.filter(user=user, code=code)
        if email_verification.exists() and not email_verification.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))
