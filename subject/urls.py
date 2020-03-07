from django.urls import path, re_path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='subject_index'),
    url(r'^delete', views.delete, name='subject_delete'),

    # path('categories', views.search, name='search'),
    # path('categories/<int:id>', views.view, name='view')
]
