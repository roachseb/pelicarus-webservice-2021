from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('updatelist', views.updatemailchimplist, name='updatelist'),
    path('members', views.listinfo, name='test')
]
