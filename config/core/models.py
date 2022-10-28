import datetime

import django.contrib.auth
from django.db import models
from ordered_model.models import OrderedModel
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


# Create your models here.

class Material(OrderedModel):
    code_material = models.CharField(max_length=64, unique=True, verbose_name=_('code'))
    description = models.TextField(max_length=64, verbose_name=_('description'))

    def __str__(self):
        return self.code_material


class Box(OrderedModel):
    code_box = models.CharField(
        max_length=24,
        unique=True, verbose_name=_('code'),
        validators=[MinLengthValidator(24)])
    description = models.TextField(max_length=64, verbose_name=_('description'))
    is_empty = models.BooleanField(default=False, verbose_name=_('empty'))

    def __str__(self):
        return self.code_box


class Appontment(OrderedModel):
    box = models.ForeignKey(
        Box, on_delete=models.PROTECT, related_name="log_box", verbose_name=_('box'))

    material = models.ForeignKey(
        Material, on_delete=models.PROTECT, related_name="log_material", verbose_name=_('material'))

    creator = models.ForeignKey(User, on_delete=models.PROTECT, editable=False, verbose_name=_('creator'))

    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    def __str__(self):
        return f'{self.box} - {self.material}'

    def created_updated(model, request):
        # obj = model.objects.latest('pk')
        obj = model
        if (obj.creator is None) or (obj.creator == ""):
            obj.creator = request.user
        obj.updated_by = request.user
        obj.save()
