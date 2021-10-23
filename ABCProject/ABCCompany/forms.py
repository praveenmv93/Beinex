from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import UserRegistration


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = UserRegistration
        fields = ("username", "first_name", 'email', 'user_image', 'mobile', 'Address')

    def clean_EMAIL(self):
        # cleaned_data = super().clean()
        # email = cleaned_data.get("email")
        email = self.cleaned_data.get("email")
        instances = UserRegistration.objects.filter(email=email)
        if instances.count() > 0:
            raise ValidationError("This Email is already taken")

        return email

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        email = self.cleaned_data["email"]
        user.email = self.cleaned_data["email"]
        user.is_employee = True

        if commit:
            user.save()
        return user


class EmpLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=50,widget=forms.PasswordInput)


class NumWordForm(forms.Form):
    number = forms.IntegerField()
