from django.contrib import admin

from .models import Person, Phone


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name")
    list_filter = ("first_name", "last_name")
    search_fields = ("first_name__startswith", "last_name__startswith", )


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ("id", "phone", "person")
    list_filter = ("phone",)
    search_fields = ("phone__startswith",)
