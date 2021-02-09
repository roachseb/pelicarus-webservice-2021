from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='helloasso'),
    path('actions/',views.actions,name='actions'),
    path('organisms/',views.organisms,name='organisms'),
    path('campaigns/',views.campaigns,name='campaigns'),
    path('payments/',views.payments,name='payments'),
    path('actions/subscribed',views.actions_subscribed,name='action_subscribed')
]