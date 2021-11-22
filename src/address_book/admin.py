from django.contrib import admin

from .models import Person, Phone


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "gender")
    list_filter = ("first_name", "last_name", "gender")
    search_fields = ("first_name__startswith", "last_name__startswith", )


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ("phone", "person")
    list_filter = ("person",)
    search_fields = ("phone__startswith",)
