from django.db import models

# Create your models here.


class RoomType(models.Model):
    room_type = models.CharField(max_length=50)
    capacity_adults = models.IntegerField()
    capacity_children = models.IntegerField()
    bed_choice = (
        ('Twins bed', 'Twins bed'),
        ('King bed', 'King bed')
    )
    bed = models.CharField(max_length=25, choices=bed_choice)
    bathhub = models.BooleanField(default=True)
    view = models.CharField(max_length=50)
    pillow_menu = models.BooleanField(default=True)
    balcone = models.BooleanField(default=True)
    wifi = models.BooleanField(default=True)
    gym_pool = models.BooleanField(default=True)
    img_detail_rooms1 = models.ImageField(upload_to='upload/roomType/', blank=True, null=True, default='Image/roomType/Default/engin-akyurt-7VopMuTM9Ms-unsplash-1024x683.jpeg')
    img_detail_rooms2 = models.ImageField(upload_to='upload/roomType/', blank=True, null=True, default='Image/roomType/Default/julian-hochgesang-nqZv8jtwLTY-unsplash-1024x683.jpeg')
    img_detail_rooms3 = models.ImageField(upload_to='upload/roomType/', blank=True, null=True, default='Image/roomType/Default/mateo-fernandez-XTC538P_eWk-unsplash-768x1024.jpeg')
    img_detail_rooms4 = models.ImageField(upload_to='upload/roomType/', blank=True, null=True, default='Image/roomType/Default/radoslav-bali-X5P-0qUQS50-unsplash-819x1024.jpeg')
    img_detail_rooms5 = models.ImageField(upload_to='upload/roomType/', blank=True, null=True, default='Image/roomType/Default/yann-maignan-376909-unsplash-1024x683.jpeg')
    area = models.IntegerField()
    img_vertical = models.ImageField(upload_to='upload/roomType/roomIntro', blank=True, null=True, default='Image/')
    img_horizontal = models.ImageField(upload_to='upload/roomType/roomIntro', blank=True, null=True, default='Image/')
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.room_type


class Room(models.Model):
    status = (
        ('Active', 'Active'),
        ('Repair', 'Repair')
    )
    room_type_ID = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10, unique=True)
    status = models.CharField(max_length=10, choices=status)

    def __str__(self):
        return self.room_number
