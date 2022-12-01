from django.urls import path
from .views import base,page1,people

urlpatterns=[
    path('',base,name='boshsahifa'),
    path('page/', page1, name="page_one"),
    path('position/', people, name="posi_tion"),

]