from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('img/', views.main),
    path('final/', views.aza)
]
