from django.contrib import admin

from .models import Contact  # Address, ContactProfile, Person, Phone, Url


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone", )


"""
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "gender")
    list_filter = ("first_name", "last_name", "gender")
    search_fields = ("first_name__startswith", "last_name__startswith", )


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ("person", "phone")
    list_filter = ("person", "phone")
    search_fields = ("person__startswith", "phone__startswith")


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("country", "city", "street", "house_number")
    list_filter = ("country", "city", "street")
    search_fields = ("country__startswith", "city__startswith", "street__startswith")


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ("link", "url", "person")
    list_filter = ("person", "link")
    search_fields = ("person__startswith", "link__startswith",)


@admin.register(ContactProfile)
class ContactProfileAdmin(admin.ModelAdmin):
    list_display = ("person", "address", "phone")
    list_filter = ("person", "phone")
    search_fields = ("person__startswith", "phone__startswith")
"""
