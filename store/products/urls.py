from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('kitchen-items/', views.product_sorts),
]
