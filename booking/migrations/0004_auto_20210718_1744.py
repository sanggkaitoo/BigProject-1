# Generated by Django 3.2.4 on 2021-07-18 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_alter_customer_contactnum'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='adults',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='booking',
            name='children',
            field=models.IntegerField(default=1),
        ),
    ]