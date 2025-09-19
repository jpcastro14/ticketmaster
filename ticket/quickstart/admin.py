from django.contrib import admin
from .models import Ticket, Sector

# Register your models here.

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display =(['title'])

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display=(['name'])