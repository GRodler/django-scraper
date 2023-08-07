from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('information/', views.take_info, name='info'),
    path('resume/',views.give_info, name='resume')
]