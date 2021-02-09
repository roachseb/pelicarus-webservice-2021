from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('filldb',views.filldatabase,name='psql_helloasso_update'),
    path('updatedb',views.updatememberdate,name='psql_update_date'),
    path('updatemailchimp',views.updatemailchimp,name='mailchimp_update'),
    path('test',views.send_active_member_info,name='gmail_active_members')
]