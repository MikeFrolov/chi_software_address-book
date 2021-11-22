from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Person(models.Model):
    first_name = models.CharField("Name", max_length=200)
    last_name = models.CharField("Surname", max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Phone(models.Model):
    phone = PhoneNumberField("Phone", null=False, blank=True, unique=True, default=None)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="phones")

    def __str__(self):
        return f"{self.phone}"
