from django.shortcuts import render
from django.views import View
from base import models as base
from room import models as room
from booking import models as booking
from datetime import datetime

# Create your views here.


def bookingConfirm(request):
    if request.method == "POST":
        check_in_date = datetime.strptime(request.POST.get('check_in_date'), "%d-%m-%Y").date()
        check_out_date = datetime.strptime(request.POST.get('check_out_date'), "%d-%m-%Y").date()
        night_amount = (check_out_date - check_in_date).days
        room_type_all = room.RoomType.objects.all()
        total_room = room.Room.objects.all()

        rooms_amount = request.POST.get('rooms_amount')

        booking_data = booking.Booking.objects.filter(checkout__gte=check_in_date, checkin__lte=check_out_date)

        # Objects phòng
        room_data = room.Room.objects.exclude(id__in=[o.id for o in booking_data])

        # Objects loại phòng có thể đặt
        room_type = room.RoomType.objects.filter(id__in=[o.room_type_ID.pk for o in room_data])

        # Lấy ra tên loại phòng và số lượng đặt
        list_reservation = []
        for item in room_type_all:
            temp = item.room_type
            if request.POST.get(item.room_type) is None or int(request.POST.get(item.room_type)) == 0:
                pass
            else:
                number = int(request.POST.get(item.room_type))
                list_reservation.append([temp, number])

        # Tạo list objects phòng để truyền vào context
        list_room_reservation = []
        for item in list_reservation:
            for room_item in room_data:
                i = 0
                if str(room_item.room_type_ID) == item[0]:
                    list_room_reservation.append(room_item)
                    i = i + 1
                if i == item[1]:
                    break

        # Tổng tiền phòng đặt
        total = 0
        for item in list_room_reservation:
            total = total + item.room_type_ID.price * night_amount

        # Lấy số lượng trống của mỗi loại phòng
        room_type_amount = []
        for item_type in room_type:
            i = 0
            for item in room_data:
                if item.room_type_ID.pk == item_type.pk:
                    i = i + 1
            temp = [i, item_type]
            room_type_amount.append(temp)

        return render(request, 'pages/booking-confirm.html', {'check_in_date': check_in_date,
                                                              'check_out_date': check_out_date,
                                                              'total': total,
                                                              'list_room_reservation': list_room_reservation,
                                                              'total_room': total_room,
                                                              'night_amount': night_amount})


def reservationReceived(request):
    if request.method == "POST":

        # Lấy dữ liệu khách hàng gửi lên
        customer_fname = request.POST.get('customer_fname')
        customer_lname = request.POST.get('customer_lname')
        customer_gender = request.POST.get('customer_gender')
        customer_mail = request.POST.get('customer_mail')
        customer_phone = request.POST.get('customer_phone')
        customer_id_number = request.POST.get('customer_id_number')
        customer_notes = request.POST.get('customer_notes')
        total_price = request.POST.get('total_price')
        paymentType = request.POST.get('payment_method')
        checkin = datetime.strptime(request.POST.get('check_in_date'), "%d-%m-%Y").date()
        checkout = datetime.strptime(request.POST.get('check_out_date'), "%d-%m-%Y").date()

        # Kiểm tra và lưu dữ liệu khách hàng
        if booking.Customer.objects.filter(idProof=customer_id_number).exists():
            new_customer = booking.Customer.objects.get(idProof=customer_id_number)
        else:
            new_customer = booking.Customer(
                firstName=customer_fname,
                lastName=customer_lname,
                contactNum=customer_phone,
                gender=customer_gender,
                idProof=customer_id_number,
                contactMail=customer_mail
            )
            new_customer.save()

        # Lưu hóa đơn đặt phòng
        new_payment = booking.Payment(
            amount=total_price,
            paymentType=paymentType,
            customerID=new_customer,
            checkin=checkin,
            checkout=checkout,
            note=customer_notes,
            status=True
        )

        new_payment.save()

        # Lưu dữ liệu chi tiết đơn đặt phòng
        total_room = int(request.POST.get('total_room'))
        for i in range(total_room):
            room_number = request.POST.get(str(i+1))
            children = request.POST.get('select-children-' + room_number)
            adults = request.POST.get('select-adults-' + room_number)

            room_id = room.Room.objects.get(room_number=room_number)

            new_booking_detail = booking.Booking(
                paymentID=new_payment,
                roomID=room_id,
                checkin=checkin,
                checkout=checkout,
                children=children,
                adults=adults
            )

            new_booking_detail.save()

    return render(request, 'pages/reservation-received.html', {'payment_id': new_payment})
