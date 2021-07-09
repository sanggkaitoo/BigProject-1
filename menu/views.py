from django.shortcuts import render
from django.views import View
from room import models as room
from base import models as base
from menu import models as menu


common_data = base.commonPage.objects.latest('id')


class DiningPage(View):
    def get(self, request):
        rooms_list = room.RoomType.objects.all()
        dining_data = menu.diningPage.objects.latest('id')
        aboutUs_data = base.aboutUsPage.objects.latest('id')
        dish_menu = menu.dish.objects.all()
        menu_data = menu.menu.objects.all()
        return render(request, 'pages/dining.html', {'common_data': common_data,
                                                     'rooms_list': rooms_list,
                                                     'dining_data': dining_data,
                                                     'dish_menu': dish_menu,
                                                     'aboutUs_data': aboutUs_data,
                                                     'menu_data': menu_data,
                                                     'navbar': 'dining'})
