# Generated by Django 3.0.7 on 2020-06-07 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0007_menuitem_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]