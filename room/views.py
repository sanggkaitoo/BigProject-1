from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from base import models as base
from room import models as room


common_data = base.commonPage.objects.latest('id')


class RoomsPage(ListView):
    def get(self, request):
        rooms_list = room.RoomType.objects.all()
        rooms_data = base.roomsPage.objects.latest('id')
        return render(request, 'pages/rooms.html', {'rooms_data': rooms_data,
                                                    'navbar': 'rooms',
                                                    'common_data': common_data,
                                                    'rooms_list': rooms_list})


class RoomsDetail(DetailView):
    def get(self, request, pk):
        data = room.RoomType.objects.get(pk=pk)
        rooms_list = room.RoomType.objects.all()
        return render(request, 'pages/room-part.html', {'common_data': common_data,
                                                        'rooms_list': rooms_list,
                                                        'data': data})


class SearchResults(View):
    def get(self, request):
        home_data = base.homePage.objects.latest('id')
        return render(request, 'pages/search-rooms.html', {'common_data': common_data,
                                                           'home_data': home_data})


class BookingConfirm(View):
    def get(self, request):
        home_data = base.homePage.objects.latest('id')
        return render(request, 'pages/booking-confirm.html', {'common_data': common_data,
                                                           'home_data': home_data})


def searchRoom(request):
    if request.method == "POST":
        check_in_date = request.POST.get('')
        check_out_date = request.POST.get('')
        adults_amount = request.POST.get('')
        children_amount = request.POST.get('')
    return render(request, 'search-rooms.html')