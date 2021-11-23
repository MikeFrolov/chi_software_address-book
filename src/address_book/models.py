from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField


class Address(models.Model):
    country = CountryField(blank_label='(select country)')
    city = models.CharField("City", max_length=50)
    street = models.CharField("Street", max_length=50)
    house_number = models.IntegerField(default=None)

    class Meta:
        unique_together = ("country", "city", "street", "house_number")

    def __str__(self):
        return f"{self.country} {self.city} {self.street} {self.house_number}"


class Person(models.Model):
    first_name = models.CharField("Name", max_length=200)
    last_name = models.CharField("Surname", max_length=200)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(null=False, max_length=1, choices=GENDER_CHOICES, default=None)
    address = models.ForeignKey(Address, null=False, on_delete=models.RESTRICT, related_name="address", default=None)

    class Meta:
        unique_together = ('first_name', 'last_name',)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Phone(models.Model):
    phone = PhoneNumberField("Phone", null=False, blank=True, unique=True, default=None)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="phones")

    def __str__(self):
        return f"{self.phone}"


class Url(models.Model):
    RESOURCE_CHOICES = (
        ('FB', 'Facebook'),
        ('LN', 'Linkedin'),
        ('IN', 'Instagram'),
        ('GH', 'GitHub'),
        ('JN', 'Jinni'),
        ('TW', 'Twitter'),
        ('WS', 'WebSite'),
    )
    link = models.CharField(null=False, max_length=2, choices=RESOURCE_CHOICES, default=None)
    url = models.URLField(max_length=200)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="url")

    def __str__(self):
        return f"{self.link} {self.url} {self.person}"
