from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.BusPark)
class BusParkAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'phone_number')

@admin.register(models.Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('number', 'type_of_bus')

@admin.register(models.Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'patronymic', 'job_title')

@admin.register(models.Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('date_of_flight', 'time_of_flight', 'direction')

@admin.register(models.Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('title', 'stay_1', 'stay_2')