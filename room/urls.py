from django.urls import path
from room import views

urlpatterns = [
    path('', views.RoomsPage.as_view(), name='rooms-page'),
    path('room-detail/<int:pk>', views.RoomsDetail.as_view(), name='rooms-detail'),
    path('search-results', views.searchRoom, name='search-result'),
]