from django.db import models


class commonPage(models.Model):
    logo_navbar = models.ImageField(upload_to='upload/navBar/nav_bar', blank=True, null=True, default='Image/logo/Logo.png')
    img_bg_footer = models.ImageField(upload_to='upload/navBar/nav_bar', blank=True, null=True, default='Image/homePage/EmailImage/bg-email.jpeg')
    title_footer1 = models.CharField(max_length=25, default='Get the latest offers', blank=True, null=True)
    title_footer2 = models.CharField(max_length=50, default='Sign up for our newsletter', blank=True, null=True)
    label_input_footer = models.CharField(max_length=100, default='Hear about our latest offers by signing up to our mailing list.', blank=True, null=True)


class indexPage(models.Model):
    big_title = models.CharField(max_length=50, default='Are you looking for a place to')
    text_change = models.CharField(max_length=10, default=' relax?')
    text_button = models.CharField(max_length=25, default='watch now')
    img_bg = models.ImageField(upload_to='upload/index/', blank=True, null=True, default='Image/mountain-4369049.jpeg')


class homePage(models.Model):
    img_bg_footer = models.ImageField(upload_to='upload/homePage/bg', blank=True, null=True, default='Image/portrait-of-attractive-woman-in-hotel-room-A3YMFVC.jpeg')
    big_title_header1 = models.CharField(max_length=25, default='Welcome to SaPa')
    big_title_header2 = models.CharField(max_length=25, default='The BEST place to be')
    small_title_header = models.CharField(max_length=100, default='Your most glorious moments with An Khang Hotel')
    img_bg_about_us1 = models.ImageField(upload_to='upload/homePage/aboutUs', blank=True, null=True, default='Image/homepage/AboutUs/couple-in-love-at-luxury-hotel-UF4696T.jpeg')
    img_bg_about_us2 = models.ImageField(upload_to='upload/homePage/aboutUs', blank=True, null=True, default='Image/homepage/AboutUs/sexy-lady-relaxing-with-cocktail-in-spa-chair-S8Y7ZX6.jpeg')
    img_bg_about_us3 = models.ImageField(upload_to='upload/homePage/aboutUs', blank=True, null=True, default='Image/homepage/AboutUs/woman-in-a-modern-bath-tub-W4VPJD6-1.jpeg')
    title_part_about_us = models.CharField(max_length=25, default='For luxury seekers')
    title_about_us = models.CharField(max_length=255, default='Discover a hotel that defines a new dimension of luxury. Emotional luxury.')
    title_part_quotes = models.CharField(max_length=25, default='Urban & Unique')
    title_quotes = models.CharField(max_length=100, default='The signature services and wonders of Sapa')
    small_text_quotes = models.CharField(max_length=100, default='Our accommodations are excellent for a trip with friends, family or as a couple')
    content_text_quotes = models.TextField(default='The concept and service of the best luxury hotels in Asturias in our sophisticated Urban Double and Unique Junior Suite rooms, with the possibility of enjoying a furnished terrace in our Double Urban Loft and Unique Junior Loft Suite.')
    img_signature = models.ImageField(upload_to='upload/homePage/signature', blank=True, null=True, default='Image/homepage/Quoes/Layer 2.png')
    position_writer = models.CharField(max_length=50, default='Hotel manage')
    title_rooms = models.CharField(max_length=100, default='We put a smile back on your face. Pleasing people the world over. The best surprise is no surprise.')
    img_dish = models.ImageField(upload_to='upload/homePage/dish', blank=True, null=True, default='Image/homepage/Restaurant/slider_bg.png')
    title_restaurant = models.CharField(max_length=100, default='The art of meeting your highest expectations. Life\'s better at the Garden')
    title_nearby = models.CharField(max_length=100, default='Explore & experience the magical nearby our hotel')
    small_text_nearby = models.CharField(max_length=100, default='Correspondingly during this time, there are a lot of parties, and happenings going on')
    content_text_nearby = models.TextField(default='If you visit us in low-season, which ranges between end of April to mid-June and end of October to mid-December, you will find a small sleepy village with about 5???000 locals, surrounded by a quiet beautiful nature, where the bells of the blacknose sheep on the meadows around the village are the only perceivable noise.')
    img_nearby1 = models.ImageField(upload_to='upload/homePage/nearbyPlace', blank=True, null=True, default='Image/homepage/NearbyPlace/Dinh-Fansipan---Anh-.jpeg')
    text_nearby1 = models.CharField(max_length=25, default='Fansipan Legend')
    img_nearby2 = models.ImageField(upload_to='upload/homePage/nearbyPlace', blank=True, null=True, default='Image/homepage/NearbyPlace/diem-ten-cac-cung-deo-dai-va-hiem-tro-bac-nhat-viet-nam.jpeg')
    text_nearby2 = models.CharField(max_length=25, default='?? Qu?? h??? Pass')
    img_nearby3 = models.ImageField(upload_to='upload/homePage/nearbyPlace', blank=True, null=True, default='Image/homepage/NearbyPlace/at_gioi-thieu-nha-tho-da-sapa_37402c2beb30db7c6fb0ab24af7426fc.jpeg')
    text_nearby3 = models.CharField(max_length=25, default='Sapa Stone Church')
    img_nearby4 = models.ImageField(upload_to='upload/homePage/nearbyPlace', blank=True, null=True, default='Image/homepage/NearbyPlace/sapa.jpeg')
    text_nearby4 = models.CharField(max_length=25, default='Terraces')
    small_text_offers = models.CharField(max_length=50, default='Click to get offers')
    img_offers1 = models.ImageField(upload_to='upload/homePage/offers', blank=True, null=True, default='Image/homepage/OffersImage/pillow-on-bed-NB5P3TZ-683x1024.jpeg')
    text_offers1 = models.CharField(max_length=50, default='Free Breakfast Include')
    img_offers2 = models.ImageField(upload_to='upload/homePage/offers', blank=True, null=True, default='Image/homepage/OffersImage/sophisticated-interior-with-crystal-chandelier-PS35LBM-683x1024.jpeg')
    text_offers2 = models.CharField(max_length=50, default='10% for advanced booking')
    img_offers3 = models.ImageField(upload_to='upload/homePage/offers', blank=True, null=True, default='Image/homepage/OffersImage/woven-blanket-on-bed-PMJPLRV-683x1024.jpeg')
    text_offers3 = models.CharField(max_length=50, default='15% for non refundable')


class roomsPage(models.Model):
    img_header1 = models.ImageField(upload_to='upload/roomsPage/header', blank=True, null=True, default='Image/roompage/headerImage/One-Bedroom-Alpine-Suite-Lake-View.jpeg')
    title_header1 = models.CharField(max_length=25, default='First')
    small_title_header1 = models.TextField(default='Elegant wooden parquet flooring. From the balconies, stunning mountain views can be enjoyed')
    img_header2 = models.ImageField(upload_to='upload/roomsPage/header', blank=True, null=True, default='Image/roompage/headerImage/room-standard-01.jpeg')
    title_header2 = models.CharField(max_length=25, default='Second')
    small_title_header2 = models.TextField(default='All of our accommodation options comprise luxury amenities such as tea & coffee makers, minibars')
    img_header3 = models.ImageField(upload_to='upload/roomsPage/header', blank=True, null=True, default='Image/roompage/headerImage/St-Moritz-Guest-Room.jpeg')
    title_header3 = models.CharField(max_length=25, default='Third')
    small_title_header3 = models.TextField(default='Family Suite with Matterhorn view on the top floor. Since our last renovation in 2018')
    title_our_rooms = models.TextField(default='Our spacious accommodations are excellent for a trip with friends, family or as a couple. Each accommodation is fully equipped and furnished to create a pleasant and relaxing atmosphere.')


class aboutUsPage(models.Model):
    img_bg_header = models.ImageField(upload_to='upload/aboutUsPage/header', blank=True, null=True, default='Image/aboutUSImage/slideImage/thought-catalog-344189-unsplash.jpeg')
    title_header = models.CharField(max_length=50, default='Homewood Suite <br> Make Yourself at Home')
    big_title1 = models.CharField(max_length=100, default='Get Ready to live for unlimite')
    big_title2 = models.CharField(max_length=100, default='living experience')
    img_slide1 = models.ImageField(upload_to='upload/aboutUsPage/slide', blank=True, null=True, default='Image/aboutUSImage/slideImage/dan-gold-4HG3Ca3EzWw-unsplash-1024x576.jpeg')
    img_slide2 = models.ImageField(upload_to='upload/aboutUsPage/slide', blank=True, null=True, default='Image/aboutUSImage/slideImage/engin-akyurt-7VopMuTM9Ms-unsplash-1024x683.jpeg')
    img_slide3 = models.ImageField(upload_to='upload/aboutUsPage/slide', blank=True, null=True, default='Image/aboutUSImage/slideImage/julian-hochgesang-nqZv8jtwLTY-unsplash-1024x683.jpeg')
    img_slide4 = models.ImageField(upload_to='upload/aboutUsPage/slide', blank=True, null=True, default='Image/aboutUSImage/slideImage/mateo-fernandez-XTC538P_eWk-unsplash-768x1024.jpeg')
    img_slide5 = models.ImageField(upload_to='upload/aboutUsPage/slide', blank=True, null=True, default='Image/aboutUSImage/slideImage/yann-maignan-376909-unsplash-1024x683.jpeg')
    title_rooms = models.CharField(max_length=255, default='Tune Hotels tells potential customers what they can expect when they visit ??? a beautiful and luxurious 5-star sleeping experience, at a very affordable 1-star price.')
    img_bg = models.ImageField(upload_to='upload/aboutUsPage/bg', blank=True, null=True, default='Image/aboutUSImage/slideImage/yann-maignan-376909-unsplash-1024x683.jpeg')
    img_intro1 = models.ImageField(upload_to='upload/roomsPage/intro', blank=True, null=True, default='Image/aboutUSImage/slideImage/eco-luxury.jpeg')
    tilte_intro1 = models.CharField(max_length=50, default='Luxury Redefined')
    content_intro1_1 = models.TextField(default='Leather detail shoulder contrastic colour contour stunning silhouette working peplum. Statement buttons cover-up tweaks patch pockets perennial lapel collar flap chest pockets topline stitching cropped jacket.')
    content_intro1_2 = models.TextField(default='Exercitation photo booth stumptown tote bag Banksy, elit small batch freegan sed. Craft beer elit seitan exercitation, photo booth et 8-bit kale chips proident chillwave deep v laborum. Aliquip veniam delectus, Marfa eiusmod Pinterest in do umami readymade swag. Selfies iPhone Kickstarter, drinking vinegar.')
    img_intro2 = models.ImageField(upload_to='upload/roomsPage/intro', blank=True, null=True, default='Image/aboutUSImage/slideImage/passion-hospitality.jpeg')
    tilte_intro2 = models.CharField(max_length=50, default='Experience the passion of hospitality')
    content_intro2_1 = models.TextField(default='Leather detail shoulder contrastic colour contour stunning silhouette working peplum. Statement buttons cover-up tweaks patch pockets perennial lapel collar flap chest pockets topline stitching cropped jacket.')
    content_intro2_2 = models.TextField(default='Exercitation photo booth stumptown tote bag Banksy, elit small batch freegan sed. Craft beer elit seitan exercitation, photo booth et 8-bit kale chips proident chillwave deep v laborum. Aliquip veniam delectus, Marfa eiusmod Pinterest in do umami readymade swag. Selfies iPhone Kickstarter, drinking vinegar.')
    img_intro3 = models.ImageField(upload_to='upload/roomsPage/intro', blank=True, null=True, default='Image/aboutUSImage/slideImage/new-spirit.jpeg')
    tilte_intro3 = models.CharField(max_length=50, default='Rest Journey in\nSingle step')
    content_intro3_1 = models.TextField(default='Leather detail shoulder contrastic colour contour stunning silhouette working peplum. Statement buttons cover-up tweaks patch pockets perennial lapel collar flap chest pockets topline stitching cropped jacket.')
    content_intro3_2 = models.TextField(default='Exercitation photo booth stumptown tote bag Banksy, elit small batch freegan sed. Craft beer elit seitan exercitation, photo booth et 8-bit kale chips proident chillwave deep v laborum. Aliquip veniam delectus, Marfa eiusmod Pinterest in do umami readymade swag. Selfies iPhone Kickstarter, drinking vinegar.')
    img_intro4 = models.ImageField(upload_to='upload/aboutUsPage/intro', blank=True, null=True, default='Image/diningpage/dishImage/elegant-restaurant-table-setting-service-for-P8HYX7H-768x513.jpeg')
    img_intro5 = models.ImageField(upload_to='upload/aboutUsPage/intro', blank=True, null=True, default='Image/diningpage/dishImage/fresh-salmon-with-dill-food-photography-recipe-JMQKHUY-768x1061.jpeg')


class contactPage(models.Model):
    img_bg_header = models.ImageField(upload_to='upload/contact/header', blank=True, null=True, default='Image/contactpage/header/mature-businessman-at-hotel-reception-PSCUC9L.jpeg')
    title_header = models.CharField(max_length=50, default='Hope to see you one day soon')
    content_our_address = models.CharField(max_length=100, default='04 Hoang Van Thu Street, Sa Pa<br>Lao Cai, Viet Nam')
    content_by_car = models.CharField(max_length=100, default='04 Hoang Van Thu Street, Sa Pa<br>Lao Cai, Viet Nam')
    content_by_train = models.CharField(max_length=100, default='04 Hoang Van Thu Street, Sa Pa<br>Lao Cai, Viet Nam')
    facebook = models.CharField(max_length=255, default='https://www.facebook.com/Hotel.An.Khang/')
    twitter = models.CharField(max_length=255, default='')
    zalo = models.CharField(max_length=255, default='https://zalo.me/0852662000')
    instagram = models.CharField(max_length=255, default='')
    address = models.TextField(default='04 Hoang Van Thu Street, Sa Pa, Lao Cai, Viet Nam')
    phone = models.CharField(max_length=20, default='+(84) 85 266 2000')
    email = models.EmailField(max_length=20, default='sanggkaitoo@gmail.com')