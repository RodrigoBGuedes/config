from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AppointmentFormScan, AppointmentFormVoice
from .models import Box, Material, Appointment
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from config.core.forms import AppointmentFormScan


# Create your views here.


def core_page(request):
    return render(request, "core/core.html")


def login(request):
    response = redirect('core_page')
    return response
    # return render(request, 'core/core.html', {})


def page_logout(request):
    if request.method == "POST":
        logout(request)

    return redirect("/")


@login_required
def appointment_scan(request):
    form_scan = AppointmentFormScan(request.POST or None)
    if request.method == 'POST':
        if form_scan.is_valid():
            new_appointment = form_scan.save(commit=False)
            new_appointment.box = Box.objects.filter(code_box=form_scan.cleaned_data['box']).first()
            new_appointment.material = Material.objects.filter(code_material=form_scan.cleaned_data['material']).first()
            new_appointment.creator = request.user
            new_appointment.save()
            Box.objects.filter(code_box=form_scan.cleaned_data['box']).update(is_empty=False)
            form_scan = AppointmentFormScan()
            messages.success(request, _('Appointment Done'))

    context = {'form_scan': form_scan}
    return render(request, 'core/appointment_scan.html', context)


@login_required
def appointment_voice(request):
    form_voice = AppointmentFormVoice(request.POST or None)
    if request.method == 'POST':
        if form_voice.is_valid():
            box_code = form_voice.cleaned_data['box']
            new_appointment = form_voice.save(commit=False)
            new_appointment.box = Box.objects.filter(code_box__endswith=box_code).first()
            new_appointment.material = Material.objects.filter(
                code_material=form_voice.cleaned_data['material']).first()
            new_appointment.creator = request.user
            new_appointment.save()
            Box.objects.filter(code_box__endswith=box_code).update(is_empty=False)
            form_voice = AppointmentFormVoice()
            messages.success(request, 'Appointment Done')

    context = {'form_voice': form_voice}
    return render(request, 'core/appointment_voice.html', context)
