# Generated by Django 3.0.7 on 2020-06-07 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantstaff',
            name='username',
            field=models.SlugField(max_length=25),
        ),
    ]
