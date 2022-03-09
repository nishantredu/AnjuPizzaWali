from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('',views.index, name='home'),
    path('bookmeal/', views.bookmeal, name='bookmeal'),
    path('combos/', views.combos, name='combos'),
    path('tracking/',views.tracking, name='tracking'),
    path('<int:cfpb>/<int:id>/', views.checkout, name='bookmeal'),
    path('booked/', views.booked,name='booked'),
    path('tracked/',views.tracked, name='tracked')
]