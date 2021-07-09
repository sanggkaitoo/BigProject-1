from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from base import models as base
from room import models as room
from booking import models as booking
from datetime import datetime
from operator import itemgetter


common_data = base.commonPage.objects.latest('id')


class RoomsPage(ListView):
    def get(self, request):
        rooms_data = base.roomsPage.objects.latest('id')
        return render(request, 'pages/rooms.html', {'rooms_data': rooms_data,
                                                    'navbar': 'rooms'})


class RoomsDetail(DetailView):
    def get(self, request, pk):
        data = room.RoomType.objects.get(pk=pk)
        return render(request, 'pages/room-part.html', {'data': data})


# class SearchResults(View):
#     def get(self, request):
#         home_data = base.homePage.objects.latest('id')
#         return render(request, 'pages/search-rooms.html', {'home_data': home_data})
#
#
# class BookingConfirm(View):
#     def get(self, request):
#         home_data = base.homePage.objects.latest('id')
#         return render(request, 'pages/booking-confirm.html', {'home_data': home_data})


def searchRoom(request):
    if request.method == "POST":
        check_in_date = datetime.strptime(request.POST.get('check_in_date'), "%d-%m-%Y").date()
        check_out_date = datetime.strptime(request.POST.get('check_out_date'), "%d-%m-%Y").date()
        adults_amount = int(request.POST.get('adults_amount'))
        children_amount = int(request.POST.get('children_amount'))
        rooms_amount = int(request.POST.get('rooms_amount'))

        booking_data = booking.Booking.objects.filter(checkout__gte=check_in_date, checkin__lte=check_out_date)

        room_data = room.Room.objects.exclude(id__in=[o.id for o in booking_data])

        room_type = room.RoomType.objects.filter(id__in=[o.room_type_ID.pk for o in room_data])

        # Lấy số lượng trống của mỗi loại phòng
        room_type_amount = []
        for item_type in room_type:
            i = 0
            for item in room_data:
                if item.room_type_ID.pk == item_type.pk:
                    i = i + 1
            temp = [i, item_type]
            room_type_amount.append(temp)

        recommend_room = []
        # Lấy ra loại phòng recommend với từng trường hợp
        if rooms_amount <= max([o[0] for o in room_type_amount]):
            for i in room_type_amount:
                if i[0] >= rooms_amount:
                    temp = [rooms_amount, room.RoomType.objects.all()[room_type_amount.index(i)]]
                    recommend_room.append(temp)
                    break
        else:
            sort = sorted(room_type_amount, key=itemgetter(0))
            count = rooms_amount
            i = 0
            while count != 0:
                count = count - sort[i][0]
                temp = [sort[i][0], sort[i][1]]
                recommend_room.append(temp)
                i = i + 1

        # Tính tổng giá tiền recommend
        total = 0
        for i in recommend_room:
            total = total + i[0]*i[1].price

        return render(request, 'pages/search-rooms.html', {'recommend_room': recommend_room,
                                                           'total': total,
                                                           'room_type_amount': room_type_amount,
                                                           'check_in_date': check_in_date,
                                                           'check_out_date': check_out_date,
                                                           'rooms_amount': rooms_amount})
