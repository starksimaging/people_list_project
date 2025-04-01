from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_view, name='home'),  # this calls my_view function and uses http://127.0.0.1:8000/
    path('myview', views.my_view, name='myview'), # this calls my_view function as well and uses http://127.0.0.1:8000/myview
    path('about', views.about_view, name='about'),
    path('location', views.location_view, name='location'),
    path('welcome', views.welcome_view, name='welcome'),
    path('people', views.person_list, name='person_list')

]