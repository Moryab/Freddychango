from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    correo_electronico = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'correo_electronico', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['correo_electronico']
        if commit:
            user.save()
        return user
