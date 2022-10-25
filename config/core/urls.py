from django.urls import path

from config.core import views
from config.core.views import login, appontment_creator
from django.conf import settings

app_name = 'core'
urlpatterns = [
    path('', login, name='core'),
    path('appontment/', appontment_creator, name='appontment'),
]
