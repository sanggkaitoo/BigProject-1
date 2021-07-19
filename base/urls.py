from django.urls import path, include
from base import views

urlpatterns = [
    path('', views.Index, name='index-page'),
    path('home/', views.HomePage.as_view(), name='home-page'),
    path('rooms/', include('room.urls')),
    path('dining/', include('menu.urls')),
    path('about-us/', views.AboutUsPage.as_view(), name='aboutUs-page'),
    path('contact/', views.ContactPage.as_view(), name='contact-page'),
    path('booking-confirmation/', include('booking.urls')),
]