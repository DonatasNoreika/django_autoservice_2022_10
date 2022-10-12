from .models import UzsakymoKomentaras
from django import forms

class UzsakymoKomentarasForm(forms.ModelForm):
    class Meta:
        model = UzsakymoKomentaras
        fields = ('uzsakymas', 'vartotojas', 'komentaras',)
        widgets = {'uzsakymas': forms.HiddenInput(), 'vartotojas': forms.HiddenInput()}
