# Generated by Django 3.0.7 on 2020-06-07 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starts', models.DateTimeField()),
                ('ends', models.DateTimeField()),
                ('number_of_people', models.PositiveIntegerField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.Guest')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('opens_at', models.TimeField(null=True)),
                ('closes_at', models.TimeField(null=True)),
                ('tables', models.PositiveIntegerField()),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('capacity', models.PositiveIntegerField()),
                ('ocupied', models.BooleanField(default=False)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='ReservedTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.Reservation')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.Table')),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.Restaurant'),
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.FloatField(default=0)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.Restaurant')),
            ],
            options={
                'unique_together': {('slug', 'restaurant')},
            },
        ),
    ]
