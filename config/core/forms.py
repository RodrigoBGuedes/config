import json

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Box, Appontment, User, Material
from django import forms


class AppontmentForm(forms.ModelForm):
    box = forms.CharField(min_length=24, max_length=24, required=True, label='Box Number')

    material = forms.CharField(max_length=64, required=True, label='Material Number')

    class Meta:
        model = Appontment
        exclude = ["box", "material"]

    def clean_box(self):
        b = self.cleaned_data['box']
        if not Box.objects.filter(code_box=b).exists():
            raise forms.ValidationError(_("The box you entered is invalid"))

        return b

    def clean_material(self):
        m = self.cleaned_data['material']
        if not Material.objects.filter(code_material=m).exists():
            raise forms.ValidationError(_("The Material you entered is invalid"))

        return m
