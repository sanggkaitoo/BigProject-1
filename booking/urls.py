from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.bookingConfirm, name='booking-confirm'),
    path('reservation-received/', views.reservationReceived, name='reservation-received'),
]