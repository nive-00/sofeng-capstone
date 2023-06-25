from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='announcments-home'),
    path('about/', views.about, name='announcments-about'),
]
