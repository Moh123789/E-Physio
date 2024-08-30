"""
URL configuration for py3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from physio import views

urlpatterns = [
    path('layout', views.layout, name='layout'),
    path('home', views.home, name='home'),
    path('physio_registration', views.physio_registration, name='physio_registration'),
    path('physio_store', views.physio_store, name='physio_store'),
    path('physio_login', views.physio_login, name='physio_login'),
    path('login_check', views.login_check, name='login_check'),
    path('physio_logout', views.physio_logout, name='physio_logout'),
    path('edit_physio_details', views.edit_physio_details, name='edit_physio_details'),
    path('physio_update/<int:id>', views.physio_update, name='physio_update'),
    path('services', views.services, name='services'),
    path('services_store', views.services_store, name='services_store'),
    path('all_services', views.all_services, name='all_services'),
    path('delete_services/<int:id>', views.delete_services, name='delete_services'),
    path('edit_services/<int:id>', views.edit_services, name='edit_services'),
    path('update_services/<int:id>', views.update_services, name='update_services'),
    path('manage_physio', views.manage_physio, name='manage_physio'),
    path('manage_physio_store', views.manage_physio_store, name='manage_physio_store'),
    path('user_appointment', views.user_appointment, name='user_appointment'),
    path('apply_appointment/<int:id>', views.apply_appointment, name='apply_appointment'),
    path('apply_appointment_store/<int:id>', views.apply_appointment_store, name='apply_appointment_store'),
    path('my_apply_appointment', views.my_apply_appointment, name='my_apply_appointment'),

    

]
