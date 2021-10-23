from django.contrib.auth.models import AbstractUser
from django.db import models

sex = (('Male', 'Male'), ('FeMale', 'FeMale'), ('Others', 'Others'),)


# Create your models here.

class UserRegistration(AbstractUser):
    user_image = models.ImageField(upload_to="uploads/")
    is_employee = models.BooleanField(default=False)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=50, choices=sex,blank=True, null=True)
    Address = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.first_name)
