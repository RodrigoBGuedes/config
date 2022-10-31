from django.urls import path

from config.core import views
from config.core.views import login, core_page
from django.conf import settings

app_name = 'core'
urlpatterns = [
    path('', core_page, name='core_page'),
]
