from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users maust have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email = email, name = name)

        user.set_password(password)
        user.save()

        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_stuff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email

# Create your models here.

class message(models.Model):
    text = models.CharField(max_length=500)
    sender = models.ForeignKey(to='UserAccount', on_delete=models.CASCADE)
    conv = models.ForeignKey(to='conversation', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class conversation(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class User_conv(models.Model):
    sender = models.ForeignKey(to='UserAccount', on_delete=models.CASCADE)
    conv = models.ForeignKey(to='conversation', on_delete=models.CASCADE)
    def __str__(self):
        return self.name