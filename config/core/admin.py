from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from config.core.models import Material, Box, Appontment


# Register your models here.

@admin.register(Material)
class Material(OrderedModelAdmin):
    list_display = ('code_material', 'description', 'move_up_down_links')


@admin.register(Box)
class Box(OrderedModelAdmin):
    list_display = ('code_box', 'description', 'is_empty', 'move_up_down_links')

    class Media:
        js = ['js/scripts.js', 'js/jquery.min.js']


@admin.register(Appontment)
class AppontmentAdmin(OrderedModelAdmin):
    list_display = (
        'created',
        'box',
        'material',
        'creator',
    )

    readonly_fields = ('created', 'creator')

    fieldsets = (
        (None, {
            'fields': ('box', 'material')
        }),
        ('Log', {
            'classes': ('collapse',),
            'fields': ('created', 'creator')
        })
    )

    def save_model(self, request, obj, form, change):
        # Passar request como argumento.
        obj.created_updated(request)
        super().save_model(request, obj, form, change)
