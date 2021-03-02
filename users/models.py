from django.db import models

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)

class UserManager(BaseUserManager):
    def create_user(self, email, password = None):
        if not email:
            raise ValueError("No Email Found")
        else:
            user = self.model(
                email = self.normalize_email(email)
            )
            user.set_password(password)
            user.save(using = self._db)
            return user
    
    def create_superuser(self, email, password = None):
        user = self.create_user(email, password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(unique = True, max_length=254)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, object = None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30, blank=True)
    lastname = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    alt_phone = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=254, blank=True)
    address2 = models.CharField(max_length=255, blank = True)
    city = models.CharField(max_length=30, blank=True)
    verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.email

    