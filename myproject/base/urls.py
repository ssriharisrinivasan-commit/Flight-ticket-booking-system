from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('booking/',booking,name='booking'),
    path('history/',history,name='history'),
    path('profile/',profile,name='profile'),
    path('logout/',logout,name='logout'),
    path('support/',support,name='support'),
    path('about/',about,name='about'),
    path('ticketbooking/<int:pk>', ticketbooking , name = 'ticketbooking'),
    path('tupdate/<int:pk>', tupdate , name = 'tupdate'),
    path('tdelete/<int:pk>', tdelete , name = 'tdelete'),
    path('viewticket/<int:pk>', viewticket , name = 'viewticket'),
]