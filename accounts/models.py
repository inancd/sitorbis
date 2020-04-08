from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.conf import settings

# Create your models here.

class AccountManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


SEX = (
    ('', 'Sex...'),
    ('ML', 'Male'),
    ('WM', 'Woman'),
    ('PR', 'Private')
)
class Account(AbstractBaseUser):
    email = models.EmailField(max_length=60, unique=True, verbose_name='Email')
    username = models.CharField(max_length=30, unique=True, verbose_name='Username')
    fullname = models.CharField(max_length=30, unique=True, verbose_name='Full Name')
    is_terms = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = AccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Profile(models.Model):
    author = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='profile/default.jpg', blank=True, upload_to='profile/%Y/%m/%d/')
    birth_day = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=20, choices=SEX, default='1', blank=True, null=True)
    websites = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.author.username

