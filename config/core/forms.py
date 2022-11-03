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
            raise forms.ValidationError(_("The box is invalid"))
        if Box.objects.filter(code_box=b, is_empty=False):
            raise forms.ValidationError(_("The box {b} is not empty").format(b=b))

        return b

    def clean_material(self):
        m = self.cleaned_data['material']
        if not Material.objects.filter(code_material=m).exists():
            raise forms.ValidationError(_("The Material is invalid"))

        return m


class AppointmentFormVoice(forms.ModelForm):
    box = forms.CharField(min_length=4, max_length=4, required=True, label='Box Number')

    material = forms.CharField(max_length=64, required=True, label='Material Number')

    class Meta:
        model = Appointment
        exclude = ["box", "material"]

    def clean_box(self):
        b = self.cleaned_data['box']
        get_boxes = Box.objects.filter(code_box__endswith=b)  # get_boxes é uma lista
        if get_boxes:
            if len(get_boxes) > 1:
                box_list = ""
                for boxes in get_boxes:
                    box_list += f"{boxes.code_box}, "
                raise forms.ValidationError(_(
                    "There's more than 1 box with {b}: \n {box_list}").format(b=b, box_list=box_list)
                                            )
            elif get_boxes.filter(is_empty=False):
                box_list = ""
                for boxes in get_boxes:
                    box_list += f"{boxes.code_box}, "
                raise forms.ValidationError(_("The box {box_list} is not empty").format(box_list=box_list))
        else:
            raise forms.ValidationError(_("The box is invalid"))

        return b

    def clean_material(self):
        m = self.cleaned_data['material']
        if not Material.objects.filter(code_material=m).exists():
            raise forms.ValidationError(_("The Material is invalid"))

        return m
