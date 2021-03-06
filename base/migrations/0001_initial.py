# Generated by Django 3.2.4 on 2021-07-18 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aboutUsPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_bg_header', models.ImageField(blank=True, default='Image/aboutUSImage/slideImage/thought-catalog-344189-unsplash.jpeg', null=True, upload_to='upload/aboutUsPage/header')),
                ('title_header', models.CharField(default='Homewood Suite <br> Make Yourself at Home', max_length=50)),
                ('big_title1', models.CharField(default='Get Ready to live for unlimite', max_length=100)),
                ('big_title2', models.CharField(default='living experience', max_length=100)),
                ('img_slide1', models.ImageField(blank=True, default='Image/aboutUSImage/slideImage/dan-gold-4HG3Ca3EzWw-unsplash-1024x576.jpeg', null=True, upload_to='upload/aboutUsPage/slide')),
                ('img_slide2', models.ImageField(blank=True, default='Image/aboutUSImage/slideImage/engin-akyurt-7VopMuTM9Ms-unsplash-1024x683.jpeg', null=True, upload_to='upload/aboutUsPage/slide')),
                ('img_slide3', models.ImageField(blank=True, default='Image/aboutUSImage/slideImage/julian-hochgesang-nqZv8jtwLTY-unsplash-1024x683.jpeg', null=True, upload_to='upload/aboutUsPage/slide')),
                ('img_slide4', models.ImageField(blank=True, default='Image/aboutUSImage/slideImage/mateo-fernandez-XTC538P_eWk-unsplash-768x1024.jpeg', null=True, upload_to='upload/aboutUsPage/slide')),
                ('img_slide5', models.ImageField(blank=True, default='Image/aboutUSImage/slideImage/yann-maignan-376909-unsplash-1024x683.jpeg', null=True, upload_to='upload/aboutUsPage/slide')),
                ('title_rooms', models.CharField(default='Tune Hotels tells potential customers what they can expect when they visit ??? a beautiful and luxurious 5-star sleeping experience, at a very affordable 1-star price.', max_length=255)),
                ('img_bg', models.ImageField(blank=True, default='Image/aboutUSImage/slideImage/yann-maignan-376909-unsplash-1024x683.jpeg', null=True, upload_to='upload/aboutUsPage/bg')),
                ('img_intro1', models.ImageField(blank=True, default='Image/aboutUSImage/slideImage/eco-luxury.jpeg', null=True, upload_to='upload/roomsPage/intro')),
                ('tilte_intro1', models.CharField(default='Luxury Redefined', max_length=50)),
                ('content_intro1_1', models.TextField(default='Leather detail shoulder contrastic colour contour stunning silhouette working peplum. Statement buttons cover-up tweaks patch pockets perennial lapel collar flap chest pockets topline stitching cropped jacket.')),
                ('content_intro1_2', models.TextField(default='Exercitation photo booth stumptown tote bag Banksy, elit small batch freegan sed. Craft beer elit seitan exercitation, photo booth et 8-bit kale chips proident chillwave deep v laborum. Aliquip veniam delectus, Marfa eiusmod Pinterest in do umami readymade swag. Selfies iPhone Kickstarter, drinking vinegar.')),
                ('img_intro2', models.ImageField(blank=True, default='Image/aboutUSImage/slideImage/passion-hospitality.jpeg', null=True, upload_to='upload/roomsPage/intro')),
                ('tilte_intro2', models.CharField(default='Experience the passion of hospitality', max_length=50)),
                ('content_intro2_1', models.TextField(default='Leather detail shoulder contrastic colour contour stunning silhouette working peplum. Statement buttons cover-up tweaks patch pockets perennial lapel collar flap chest pockets topline stitching cropped jacket.')),
                ('content_intro2_2', models.TextField(default='Exercitation photo booth stumptown tote bag Banksy, elit small batch freegan sed. Craft beer elit seitan exercitation, photo booth et 8-bit kale chips proident chillwave deep v laborum. Aliquip veniam delectus, Marfa eiusmod Pinterest in do umami readymade swag. Selfies iPhone Kickstarter, drinking vinegar.')),
                ('img_intro3', models.ImageField(blank=True, default='Image/aboutUSImage/slideImage/new-spirit.jpeg', null=True, upload_to='upload/roomsPage/intro')),
                ('tilte_intro3', models.CharField(default='Rest Journey in\nSingle step', max_length=50)),
                ('content_intro3_1', models.TextField(default='Leather detail shoulder contrastic colour contour stunning silhouette working peplum. Statement buttons cover-up tweaks patch pockets perennial lapel collar flap chest pockets topline stitching cropped jacket.')),
                ('content_intro3_2', models.TextField(default='Exercitation photo booth stumptown tote bag Banksy, elit small batch freegan sed. Craft beer elit seitan exercitation, photo booth et 8-bit kale chips proident chillwave deep v laborum. Aliquip veniam delectus, Marfa eiusmod Pinterest in do umami readymade swag. Selfies iPhone Kickstarter, drinking vinegar.')),
                ('img_intro4', models.ImageField(blank=True, default='Image/diningpage/dishImage/elegant-restaurant-table-setting-service-for-P8HYX7H-768x513.jpeg', null=True, upload_to='upload/aboutUsPage/intro')),
                ('img_intro5', models.ImageField(blank=True, default='Image/diningpage/dishImage/fresh-salmon-with-dill-food-photography-recipe-JMQKHUY-768x1061.jpeg', null=True, upload_to='upload/aboutUsPage/intro')),
            ],
        ),
        migrations.CreateModel(
            name='commonPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_navbar', models.ImageField(blank=True, default='Image/logo/Logo.png', null=True, upload_to='upload/navBar/nav_bar')),
                ('img_bg_footer', models.ImageField(blank=True, default='Image/homePage/EmailImage/bg-email.jpeg', null=True, upload_to='upload/navBar/nav_bar')),
                ('title_footer1', models.CharField(blank=True, default='Get the latest offers', max_length=25, null=True)),
                ('title_footer2', models.CharField(blank=True, default='Sign up for our newsletter', max_length=50, null=True)),
                ('label_input_footer', models.CharField(blank=True, default='Hear about our latest offers by signing up to our mailing list.', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='contactPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_bg_header', models.ImageField(blank=True, default='Image/contactpage/header/mature-businessman-at-hotel-reception-PSCUC9L.jpeg', null=True, upload_to='upload/contact/header')),
                ('title_header', models.CharField(default='Hope to see you one day soon', max_length=50)),
                ('content_our_address', models.CharField(default='04 Hoang Van Thu Street, Sa Pa<br>Lao Cai, Viet Nam', max_length=100)),
                ('content_by_car', models.CharField(default='04 Hoang Van Thu Street, Sa Pa<br>Lao Cai, Viet Nam', max_length=100)),
                ('content_by_train', models.CharField(default='04 Hoang Van Thu Street, Sa Pa<br>Lao Cai, Viet Nam', max_length=100)),
                ('facebook', models.CharField(default='https://www.facebook.com/Hotel.An.Khang/', max_length=255)),
                ('twitter', models.CharField(default='', max_length=255)),
                ('zalo', models.CharField(default='https://zalo.me/0852662000', max_length=255)),
                ('instagram', models.CharField(default='', max_length=255)),
                ('address', models.TextField(default='04 Hoang Van Thu Street, Sa Pa, Lao Cai, Viet Nam')),
                ('phone', models.CharField(default='+(84) 85 266 2000', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='homePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_bg_footer', models.ImageField(blank=True, default='Image/portrait-of-attractive-woman-in-hotel-room-A3YMFVC.jpeg', null=True, upload_to='upload/homePage/bg')),
                ('big_title_header1', models.CharField(default='Welcome to SaPa', max_length=25)),
                ('big_title_header2', models.CharField(default='The BEST place to be', max_length=25)),
                ('small_title_header', models.CharField(default='Your most glorious moments with An Khang Hotel', max_length=100)),
                ('img_bg_about_us1', models.ImageField(blank=True, default='Image/homepage/AboutUs/couple-in-love-at-luxury-hotel-UF4696T.jpeg', null=True, upload_to='upload/homePage/aboutUs')),
                ('img_bg_about_us2', models.ImageField(blank=True, default='Image/homepage/AboutUs/sexy-lady-relaxing-with-cocktail-in-spa-chair-S8Y7ZX6.jpeg', null=True, upload_to='upload/homePage/aboutUs')),
                ('img_bg_about_us3', models.ImageField(blank=True, default='Image/homepage/AboutUs/woman-in-a-modern-bath-tub-W4VPJD6-1.jpeg', null=True, upload_to='upload/homePage/aboutUs')),
                ('title_part_about_us', models.CharField(default='For luxury seekers', max_length=25)),
                ('title_about_us', models.CharField(default='Discover a hotel that defines a new dimension of luxury. Emotional luxury.', max_length=255)),
                ('title_part_quotes', models.CharField(default='Urban & Unique', max_length=25)),
                ('title_quotes', models.CharField(default='The signature services and wonders of Sapa', max_length=100)),
                ('small_text_quotes', models.CharField(default='Our accommodations are excellent for a trip with friends, family or as a couple', max_length=100)),
                ('content_text_quotes', models.TextField(default='The concept and service of the best luxury hotels in Asturias in our sophisticated Urban Double and Unique Junior Suite rooms, with the possibility of enjoying a furnished terrace in our Double Urban Loft and Unique Junior Loft Suite.')),
                ('img_signature', models.ImageField(blank=True, default='Image/homepage/Quoes/Layer 2.png', null=True, upload_to='upload/homePage/signature')),
                ('position_writer', models.CharField(default='Hotel manage', max_length=50)),
                ('title_rooms', models.CharField(default='We put a smile back on your face. Pleasing people the world over. The best surprise is no surprise.', max_length=100)),
                ('img_dish', models.ImageField(blank=True, default='Image/homepage/Restaurant/slider_bg.png', null=True, upload_to='upload/homePage/dish')),
                ('title_restaurant', models.CharField(default="The art of meeting your highest expectations. Life's better at the Garden", max_length=100)),
                ('title_nearby', models.CharField(default='Explore & experience the magical nearby our hotel', max_length=100)),
                ('small_text_nearby', models.CharField(default='Correspondingly during this time, there are a lot of parties, and happenings going on', max_length=100)),
                ('content_text_nearby', models.TextField(default='If you visit us in low-season, which ranges between end of April to mid-June and end of October to mid-December, you will find a small sleepy village with about 5???000 locals, surrounded by a quiet beautiful nature, where the bells of the blacknose sheep on the meadows around the village are the only perceivable noise.')),
                ('img_nearby1', models.ImageField(blank=True, default='Image/homepage/NearbyPlace/Dinh-Fansipan---Anh-.jpeg', null=True, upload_to='upload/homePage/nearbyPlace')),
                ('text_nearby1', models.CharField(default='Fansipan Legend', max_length=25)),
                ('img_nearby2', models.ImageField(blank=True, default='Image/homepage/NearbyPlace/diem-ten-cac-cung-deo-dai-va-hiem-tro-bac-nhat-viet-nam.jpeg', null=True, upload_to='upload/homePage/nearbyPlace')),
                ('text_nearby2', models.CharField(default='?? Qu?? h??? Pass', max_length=25)),
                ('img_nearby3', models.ImageField(blank=True, default='Image/homepage/NearbyPlace/at_gioi-thieu-nha-tho-da-sapa_37402c2beb30db7c6fb0ab24af7426fc.jpeg', null=True, upload_to='upload/homePage/nearbyPlace')),
                ('text_nearby3', models.CharField(default='Sapa Stone Church', max_length=25)),
                ('img_nearby4', models.ImageField(blank=True, default='Image/homepage/NearbyPlace/sapa.jpeg', null=True, upload_to='upload/homePage/nearbyPlace')),
                ('text_nearby4', models.CharField(default='Terraces', max_length=25)),
                ('small_text_offers', models.CharField(default='Click to get offers', max_length=50)),
                ('img_offers1', models.ImageField(blank=True, default='Image/homepage/OffersImage/pillow-on-bed-NB5P3TZ-683x1024.jpeg', null=True, upload_to='upload/homePage/offers')),
                ('text_offers1', models.CharField(default='Free Breakfast Include', max_length=50)),
                ('img_offers2', models.ImageField(blank=True, default='Image/homepage/OffersImage/sophisticated-interior-with-crystal-chandelier-PS35LBM-683x1024.jpeg', null=True, upload_to='upload/homePage/offers')),
                ('text_offers2', models.CharField(default='10% for advanced booking', max_length=50)),
                ('img_offers3', models.ImageField(blank=True, default='Image/homepage/OffersImage/woven-blanket-on-bed-PMJPLRV-683x1024.jpeg', null=True, upload_to='upload/homePage/offers')),
                ('text_offers3', models.CharField(default='15% for non refundable', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='indexPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('big_title', models.CharField(default='Are you looking for a place to', max_length=50)),
                ('text_change', models.CharField(default=' relax?', max_length=10)),
                ('text_button', models.CharField(default='watch now', max_length=25)),
                ('img_bg', models.ImageField(blank=True, default='Image/mountain-4369049.jpeg', null=True, upload_to='upload/index/')),
            ],
        ),
        migrations.CreateModel(
            name='roomsPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_header1', models.ImageField(blank=True, default='Image/roompage/headerImage/One-Bedroom-Alpine-Suite-Lake-View.jpeg', null=True, upload_to='upload/roomsPage/header')),
                ('title_header1', models.CharField(default='First', max_length=25)),
                ('small_title_header1', models.TextField(default='Elegant wooden parquet flooring. From the balconies, stunning mountain views can be enjoyed')),
                ('img_header2', models.ImageField(blank=True, default='Image/roompage/headerImage/room-standard-01.jpeg', null=True, upload_to='upload/roomsPage/header')),
                ('title_header2', models.CharField(default='Second', max_length=25)),
                ('small_title_header2', models.TextField(default='All of our accommodation options comprise luxury amenities such as tea & coffee makers, minibars')),
                ('img_header3', models.ImageField(blank=True, default='Image/roompage/headerImage/St-Moritz-Guest-Room.jpeg', null=True, upload_to='upload/roomsPage/header')),
                ('title_header3', models.CharField(default='Third', max_length=25)),
                ('small_title_header3', models.TextField(default='Family Suite with Matterhorn view on the top floor. Since our last renovation in 2018')),
                ('title_our_rooms', models.TextField(default='Our spacious accommodations are excellent for a trip with friends, family or as a couple. Each accommodation is fully equipped and furnished to create a pleasant and relaxing atmosphere.')),
            ],
        ),
    ]
