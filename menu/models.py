from django.db import models


class menu(models.Model):
    name_menu = models.CharField(max_length=100, default='Signature Menu')
    img_menu = models.ImageField(upload_to='upload/dining/menu', blank=True, null=True, default='Image/diningpage/menuImage/lunch.jpeg')

    def __str__(self):
        return self.name_menu


class dish(models.Model):
    name_menu = models.ForeignKey(menu, on_delete=models.CASCADE)
    name_food = models.CharField(max_length=100, default='Salted Fried Chicken')
    description_food = models.CharField(max_length=255, default='Mint parsley with apple cider vinegar, salt, sugar & spices')
    price_food = models.IntegerField()
    special = models.BooleanField(default=False)
    sale = models.BooleanField(default=False)
    sale_price = models.IntegerField(default=0)

    def __str__(self):
        return self.name_food


class diningPage(models.Model):
    img_bg_header = models.ImageField(upload_to='upload/diningPage/header', blank=True, null=True, default='Image/homepage/RoomImage/149368628.jpeg')
    title_header1 = models.CharField(max_length=50, default='Homewood Suite')
    title_header2 = models.CharField(max_length=50, default='Make Yourself at Home')
    img_slide1 = models.ImageField(upload_to='upload/diningPage/slide', blank=True, null=True, default='Image/diningpage/slideImage/louis-hansel-shotsoflouis-iBfVwYwA3ek-unsplash-1024x683.jpeg')
    img_slide2 = models.ImageField(upload_to='upload/diningPage/slide', blank=True, null=True, default='Image/diningpage/slideImage/the-chef-is-garnishing-appetizer-dish-PDHYM4B-683x1024.jpeg')
    img_slide3 = models.ImageField(upload_to='upload/diningPage/slide', blank=True, null=True, default='Image/diningpage/slideImage/asiya-kiev-SiwrpBnxDww-unsplash-1024x683.jpeg')
    img_slide4 = models.ImageField(upload_to='upload/diningPage/slide', blank=True, null=True, default='Image/diningpage/slideImage/fresh-salmon-with-dill-food-photography-recipe-JMQKHUY-741x1024.jpeg')
    menu1 = models.ForeignKey(menu, on_delete=models.CASCADE, related_name='menu1')
    menu2 = models.ForeignKey(menu, on_delete=models.CASCADE, related_name='menu2')
    img_intro1 = models.ImageField(upload_to='upload/diningPage/intro', blank=True, null=True, default='Image/diningpage/dishImage/fresh-salmon-with-dill-food-photography-recipe-JMQKHUY-768x1061.jpeg')
    img_intro2 = models.ImageField(upload_to='upload/diningPage/intro', blank=True, null=True, default='Image/diningpage/dishImage/elegant-restaurant-table-setting-service-for-P8HYX7H-768x513.jpeg')
