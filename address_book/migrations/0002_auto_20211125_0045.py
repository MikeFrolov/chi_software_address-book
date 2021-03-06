# Generated by Django 3.2.9 on 2021-11-25 00:45

from django.db import migrations, models

import django_countries.fields

import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('address_book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='city',
            field=models.CharField(blank=True, max_length=50, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='contact',
            name='house_number',
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default=None,
                                                                 max_length=128,
                                                                 region=None,
                                                                 unique=True,
                                                                 verbose_name='Phone'
                                                                 ),
        ),
        migrations.AlterField(
            model_name='contact',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='staticfiles/images/profile/'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='street',
            field=models.CharField(blank=True, max_length=50, verbose_name='Street'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='url',
            field=models.URLField(null=True, unique=True),
        ),
    ]
