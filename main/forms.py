from django import forms
from django.utils.translation import ugettext_lazy as _

from main.models import Hacker


class HackerForm(forms.ModelForm):
    class Meta:
        model = Hacker
        exclude = ('reputation',)


class LoginForm(forms.Form):
    nombre_usuario = forms.CharField(max_length=100)
    password = forms.CharField(label=_("Contrasenia"), widget=forms.PasswordInput)
