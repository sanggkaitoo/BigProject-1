from django.shortcuts import render
from django.views import View
from base.models import *
from room.models import *
from menu.models import *



def Index(request):
    rooms_list = RoomType.objects.all()
    index_data = indexPage.objects.latest('id')
    return render(request, 'index.html', {'index_data': index_data})


class HomePage(View):
    def get(self, request):
        aboutUs_data = aboutUsPage.objects.latest('id')
        home_data = homePage.objects.latest('id')
        return render(request, 'pages/home.html', {'home_data': home_data,
                                                   'aboutUs_data': aboutUs_data,
                                                   'navbar': 'home'})


class AboutUsPage(View):
    def get(self, request):
        dining_data = diningPage.objects.latest('id')
        aboutUs_data = aboutUsPage.objects.latest('id')
        return render(request, 'pages/about-us.html', {'aboutUs_data': aboutUs_data,
                                                       'dining_data': dining_data,
                                                       'navbar': 'aboutUs'})


class ContactPage(View):
    def get(self, request):
        rooms_list = RoomType.objects.all()
        contact_data = contactPage.objects.latest('id')
        return render(request, 'pages/contact.html', {'rooms_list': rooms_list,
                                                      'contact_data': contact_data,
                                                      'navbar': 'contact'})
