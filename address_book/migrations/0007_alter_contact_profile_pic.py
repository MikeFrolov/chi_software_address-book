# Generated by Django 3.2.9 on 2021-11-25 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address_book', '0006_alter_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='profile_pic',
            field=models.ImageField(blank=True, default='', upload_to='static/images/profile/'),
        ),
    ]