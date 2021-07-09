from base import models as base
from room import models as room
from django.http import Http404


def navbar_context_processor(request):
    try:
        common_data = base.commonPage.objects.latest('id')
    except:
        raise Http404("No data of navbar")
    return {
        'common_data': common_data,
    }


def room_list_context_processor(request):
    try:
        rooms_list = room.RoomType.objects.all()
    except:
        raise Http404("No data of room's type")
    return {
        'rooms_list': rooms_list
    }


def footer_context_processor(request):
    try:
        footer_data = base.contactPage.objects.latest('id')
    except:
        raise Http404("No footer data")
    return {
        'footer_data': footer_data
    }
