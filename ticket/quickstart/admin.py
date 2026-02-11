from django.contrib import admin
from .models import Ticket, Sector, Broker, Sales

# Register your models here.

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display =(['title'])

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display=(['name','code'])

@admin.register(Broker)
class BrokerAdmin(admin.ModelAdmin):
    list_display=(['title'])