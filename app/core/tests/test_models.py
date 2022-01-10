from django.test import TestCase

from django.contrib.auth import get_user_model


class Modeltest(TestCase):

    def test_create_user_with_email_successful(self):
        """ Test creating a new user with an email is succesfull"""
        email = "test@gmail.com"
        password = "Testpass@123"
        user = get_user_model().objects.create_user(
        email = email,
        password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test  the  email for new user is normalized"""
        email = "USERNAME@GMAI.COM"
        user  = get_user_model().objects.create_user(email, "test123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_ivalid_email(self):
        """ Test creating new user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test@123")

    def test_create_new_super_user(self):
        """ Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
        'test@gmail.com',
        'test"123'
        )

        assertTrue(user.is_superuser)
        assertTrue(user.is_staff)
        
