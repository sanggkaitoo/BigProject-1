# Generated by Django 3.2.4 on 2021-07-08 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='checkin',
            field=models.DateTimeField(default=''),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkout',
            field=models.DateTimeField(default=''),
        ),
    ]