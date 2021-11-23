from django.contrib import admin

from .models import Address, Person, Phone, Url


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "gender", "address")
    list_filter = ("first_name", "last_name", "gender")
    search_fields = ("first_name__startswith", "last_name__startswith", )


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ("phone", "person")
    list_filter = ("person",)
    search_fields = ("phone__startswith",)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("country", "city", "street", "house_number")
    list_filter = ("country", "city", "street")
    search_fields = ("country__startswith", "city__startswith", "street__startswith")


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ("link", "url", "person")
    list_filter = ("link", "person",)
    search_fields = ("link__startswith", "person__startswith",)
