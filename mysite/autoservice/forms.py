from .models import UzsakymoKomentaras, Profile
from django.contrib.auth.models import User
from django import forms

class UzsakymoKomentarasForm(forms.ModelForm):
    class Meta:
        model = UzsakymoKomentaras
        fields = ('uzsakymas', 'vartotojas', 'komentaras',)
        widgets = {'uzsakymas': forms.HiddenInput(), 'vartotojas': forms.HiddenInput()}


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nuotrauka']