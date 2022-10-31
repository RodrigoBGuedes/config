import json

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Box, Appointment, User, Material
from django import forms


class AppointmentFormScan(forms.ModelForm):
    box = forms.CharField(min_length=24, max_length=24, required=True, label='Box Number')

    material = forms.CharField(max_length=64, required=True, label='Material Number')

    class Meta:
        model = Appointment
        exclude = ["box", "material"]

    def clean_box(self):
        b = self.cleaned_data['box']
        if not Box.objects.filter(code_box=b).exists():
            raise forms.ValidationError(_(f"The box {b} is invalid"))
        if Box.objects.filter(code_box=b, is_empty=False):
            raise forms.ValidationError(_(f"The box {b} is not empty"))

        return b

    def clean_material(self):
        m = self.cleaned_data['material']
        if not Material.objects.filter(code_material=m).exists():
            raise forms.ValidationError(_(f"The Material {m} is invalid"))

        return m


class AppointmentFormVoice(forms.ModelForm):
    box = forms.CharField(min_length=4, max_length=4, required=True, label='Box Number')

    material = forms.CharField(max_length=64, required=True, label='Material Number')

    class Meta:
        model = Appointment
        exclude = ["box", "material"]

    def clean_box(self):
        b = self.cleaned_data['box']
        if not Box.objects.filter(code_box=b).exists():
            raise forms.ValidationError(_(f"The box {b} is invalid"))
        if Box.objects.filter(code_box=b, is_empty=False):
            raise forms.ValidationError(_(f"The box {b} is not empty"))

        return b

    def clean_material(self):
        m = self.cleaned_data['material']
        if not Material.objects.filter(code_material=m).exists():
            raise forms.ValidationError(_(f"The Material {m} is invalid"))

        return m