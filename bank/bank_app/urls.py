from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('single/',views.single, name='single'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('registration_form/', views.registration_form, name='registration_form'),
    path('go_to_registration_form/', views.go_to_registration_form, name='go_to_registration_form'),
]