from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import Manufacturer, Car, Driver


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]
    search_fields = ["name", "country"]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["model", "manufacturer",]
    search_fields = ["model",]
    list_filter = ["manufacturer",]


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    # відображаємо license_number як і решту
    list_display = UserAdmin.list_display + ("license_number",)

    search_fields = ["username", "email", "license_number"]

    # редагування Driver
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )

    # створення Driver
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("first_name", "last_name", "license_number",)}),
    )

