from datetime import timedelta
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from users.forms import UserRegisterForm
from users.models import EmailVerification, User


class UserRegistrationViewTestCase(TestCase):

    def setUp(self):
        self.path = reverse('users:registration')
        self.data = {
            'first_name': 'Ihor',
            'last_name': 'Ryabets',
            'username': 'drunar',
            'email': 'test@test.com',
            'password1': '12345678pP',
            'password2': '12345678pP',
        }

    def test_user_registration_get(self):
        response = self.client.get(self.path)
        form = response.context_data.get('form')

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data.get('title'), 'Store - registration')
        self.assertTemplateUsed(response, 'users/registration.html')
        self.assertIsInstance(form, UserRegisterForm)

    def test_user_registration_post_success(self):
        username = self.data.get('username')
        self.assertFalse(User.objects.filter(username=username).exists())

        response = self.client.post(self.path, self.data)

        # check creating of user
        self.assertEqual(response.status_code, HTTPStatus.FOUND)  # 302
        self.assertEqual(response.url, '/users/login/')
        self.assertTrue(User.objects.filter(username=username).exists())

        # check creating of email verification
        email_verification = EmailVerification.objects.filter(user__username=username)
        self.assertTrue(email_verification.exists())
        self.assertEqual(
            email_verification.first().expiration.date(),
            (now() + timedelta(hours=48)).date(),
        )

    def test_user_registration_post_fail(self):
        User.objects.create(username=self.data.get('username'))
        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'A user with that username already exists.', html=True)
