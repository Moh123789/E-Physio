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
from customer import views

urlpatterns = [
    path('layout', views.layout, name='layout'),
    path('about', views.about, name='about'),
    path('home', views.home, name='home'),
    path('customer_registration', views.customer_registration, name='customer_registration'),
    path('customer_store', views.customer_store, name='customer_store'),
    path('customer_edit_profile', views.customer_edit_profile, name='customer_edit_profile'),
    path('customer_update/<int:id>', views.customer_update, name='customer_update'),
    path('customer_login', views.customer_login, name='customer_login'),
    path('login_check', views.login_check, name='login_check'),
    path('customer_logout', views.customer_logout, name='customer_logout'),
    path('feedback', views.feedback, name='feedback'),
    path('feedback_store', views.feedback_store, name='feedback_store'),

    path('contact', views.contact, name='contact'),
    path('contact_store', views.contact_store, name='contact_store'),
    path('physios', views.physios, name='physios'),
    path('view_physio/<int:id>', views.view_physio, name='view_physio'),
    path('appointment/<int:id>', views.appointment, name='appointment'),
    path('appointment_store', views.appointment_store, name='appointment_store'),
    path('thankyou', views.thankyou, name='thankyou'),
    path('my_appointment', views.my_appointment, name='my_appointment'),
    path('search_beautician', views.search_beautician, name='search_beautician'),
    path('view_physio', views.view_physio, name='view_physio'),
    path('changepass', views.changepass, name='changepass'),
    path('changepass_update', views.changepass_update, name='changepass_update'),
    path('thanks', views.thanks, name='thanks'),
    path('applied_feedback', views.applied_feedback, name='applied_feedback'),

    # path('layout', views.layout, name='layout'),
    # path('dashboard', views.dashboard, name='dashboard'),
    # path('form', views.form, name='form'),
    # path('add_state', views.add_state, name='add_state'),
    # path('state_store', views.state_store, name='state_store'),
    # path('state_delete/<int:id>', views.state_delete, name='state_delete'),
    # path('state_edit/<int:id>', views.state_edit, name='state_edit'),
    # path('state_update/<int:id>', views.state_update, name='state_update'),
    

    # path('add_city', views.add_city, name='add_city'),
    # path('city_store', views.city_store, name='city_store'),
    # path('all_city', views.all_city, name='all_city'),
    # path('city_delete/<int:id>', views.city_delete, name='city_delete'),
    # path('city_edit/<int:id>', views.city_edit, name='city_edit'),
    # path('city_update/<int:id>', views.city_update, name='city_update'),

    # path('table', views.table, name='table'),
    # path('all_state', views.all_state, name='all_state'),
    # path('all_physio', views.all_physio, name='all_physio'),
    # path('all_user', views.all_user, name='all_user'),
    # path('login', views.login, name='login'),
    # path('login_check', views.login_check, name='login_check'),
    # path('logout', views.logout, name='logout'),

]
