from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('member/search/all',views.membersearchall,name='psql_member_searchall')
]