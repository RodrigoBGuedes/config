"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from config.core.views import page_logout, appointment_scan, appointment_voice, core_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('config.core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout', page_logout, name='logout'),
    path('appointment_scan', appointment_scan, name='appointment_scan'),
    path('appointment_voice', appointment_voice, name='appointment_voice'),
    path('core', core_page, name='core_page'),
]
