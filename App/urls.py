# your_app_name/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create_user/', views.create_user, name='create_user'),
    path('create_product/', views.create_product, name='create_product'),
    path('create_order/', views.create_order, name='create_order'),
]
