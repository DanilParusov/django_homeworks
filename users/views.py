import random

from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from django.conf import settings

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        self.object = form.save()
        if form.is_valid():
            code = ''.join([str(random.randint(0, 9)) for _ in range(12)])
            self.object.verification_code = code
            self.object.save()
            verification_url = reverse('users:confirm_email', args=[self.object.verification_code])
            link = self.request.build_absolute_uri(verification_url)

            send_mail(
                'Подтверждение регистрации',
                f'Пожалуйста, перейдите по ссылке для подтверждения: {link}',
                settings.DEFAULT_FROM_EMAIL,  # Отправитель
                [self.object.email],  # Получатель(и)
                fail_silently=False,
            )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('users:confirm_email', kwargs={'email': self.object.email})

class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('user:profile')

    def get_object(self, queryset=None):
        return self.request.user

def verify_email(request, email):

    users = User.objects.filter(verification_code=email)
    if len(users) > 0:
        user = users[0]
        user.is_email_verified = True
        user.save()
        return redirect(reverse('users:login'))
    else:
        raise ValidationError(f'You have used the wrong code!')