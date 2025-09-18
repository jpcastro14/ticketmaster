from django.contrib import admin
from .models import Recipe, Ticket

# Register your models here.


@admin.register(Ticket)

class TicketAdmin(admin.ModelAdmin):
    list_display =(['title'])