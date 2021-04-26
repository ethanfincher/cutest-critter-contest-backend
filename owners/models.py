from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


class UserAccountManager(BaseUserManager):
    def create_user(self, name, email, critters, image=None, password=None):
        if not email:
            raise ValueError('no email provided')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, critters=critters)

        user.set_password(password)
        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    critters = models.TextField()
    image = models.ImageField(upload_to='owner_images',
                              default=None, blank=True, null=True)
    image_url = models.TextField(default=None, blank=True, null=True)
    is_winner = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'critters', 'image', 'image_url', 'is_winner']

    def get_name(self):
        return self.name

    def __str__(self):
        return self.email
