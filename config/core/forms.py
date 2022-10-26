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
        if Box.objects.filter(code_box=b).exists():
            raise ValidationError("The box {} is already created".format(b))

        return b
