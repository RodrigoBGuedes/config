
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext_lazy as _
from .forms import AppontmentForm
from .models import Box, Material, Appontment

from config.core.forms import AppontmentForm


# Create your views here.

def login(request):
    response = redirect('/accounts/login/')
    return response
    # return render(request, 'core/core.html', {})


@login_required
def appontment_creator(request):
    form = AppontmentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_appontment = form.save(commit=False)
            new_appontment.box = Box.objects.filter(code_box=form.cleaned_data['box']).first()
            new_appontment.material = Material.objects.filter(code_material=form.cleaned_data['material']).first()
            new_appontment.creator = request.user
            new_appontment.save()
            Box.objects.filter(code_box=form.cleaned_data['box']).update(is_empty=False)
            form = AppontmentForm()

    context = {'form': form}
    return render(request, 'core/appontment.html', context)

# def appontment_create(request):
#     # template_name = 'core/appontment.html'
#
#     forms = AppontmentForm(request.POST or None)
#
#     if request.method == 'POST':
#         box_code = request.POST.get('box')
#         box_id = Box.objects.get(code_box=box_code)
#         material_code = request.POST.get('material')
#         material_id = Material.objects.get(code_material=material_code)
#         if box_code == str(Box.objects.get(code_box=box_code)) and \
#                 material_code == str(Material.objects.get(code_material=material_code)):
#             if forms.is_valid():
#                 forms.save()
#             # Appontment.objects.create(box=box_id.id, material=material_id.id, date=datetime.datetime.now(),
#             #                           user=User.objects.get(pk=3))
#         else:
#             raise ValueError(_('Something is wrong'))
#         return redirect('/appontment/')
#
#     context = {'forms': forms}
#     return render(request, 'core/appontment.html', context)
