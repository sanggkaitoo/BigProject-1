# Generated by Django 3.2.4 on 2021-07-19 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='email',
            field=models.EmailField(default='sanggkaitoo@gmail.com', max_length=20),
        ),
    ]
