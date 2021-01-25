from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    # one additional field
    email = forms.EmailField()
    # the model to be linked to and the fields to be shown
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
# to update username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']
