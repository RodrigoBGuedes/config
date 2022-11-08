from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from config.core.models import Material, Box, Appointment


# Register your models here.

@admin.register(Material)
class Material(OrderedModelAdmin):
    list_display = ('code_material', 'code_material_related', 'move_up_down_links')


@admin.register(Box)
class Box(OrderedModelAdmin):
    list_display = ('code_box', 'description', 'is_empty', 'move_up_down_links')

    class Media:
        js = ['js/scripts.js', 'js/jquery.min.js']


@admin.register(Appointment)
class AppointmentAdmin(OrderedModelAdmin):
    list_display = (
        'created',
        'box',
        'material',
        'related_material',
        'creator',
    )

    readonly_fields = ('created', 'creator')

    fieldsets = (
        (None, {
            'fields': ('box', 'material', 'related_material')
        }),
        ('Log', {
            'classes': ('collapse',),
            'fields': ('created', 'creator')
        })
    )


