from django.urls import path

from .views import *

urlpatterns =[
    path("",home,name='home'),
    path("addMembers/",addMembers,name="addMembers"),
    path("allMembers/",membersDetails,name="membersDetail"),
    path("delete/<int:pk>",deleteDetail,name="delete"),
]