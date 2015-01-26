from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class AccountManager(BaseUserManager):
    """
    Object methods for Account.
    """
    def create_user(self, email, password, **kwargs):
        """
        Create a new user instance.
        """
        if not email:
            raise ValueError('Users must have a valid email address.')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username.')

        account = self.model(
            email=self.normalize_email(email), username=kwargs.get('username')
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, username, email, password, **kwargs):
        """
        Create a new superuser instance.
        """
        account = self.create_user(username, email, password, **kwargs)

        account.is_admin = True
        account.save()

        return account


class Account(AbstractBaseUser):
    """
    Custom User instance.
    """
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __unicode__(self):
        """
        Return unicode repr as username.
        """
        return self.username

    def get_full_name(self):
        """
        Return firstname and lastname together.
        """
        return ' '.join(self.first_name, self.last_name)

    def get_short_name(self):
        """
        Return just firstname.
        """
        return self.first_name

    def get_identification(self):
        """
        If first name exists, return fullname. Otherwise, get the username.
        """
        return self.get_full_name() if self.first_name else self.username
