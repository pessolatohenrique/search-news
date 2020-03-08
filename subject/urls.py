from django.urls import path, re_path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='subject_index'),
    url(r'^create', views.create, name='subject_create'),
    url(r'^delete', views.delete, name='subject_delete')
]
