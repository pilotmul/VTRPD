from django.contrib import admin
from .models import CodeSubmission, Click,AttemptCounter
from django.utils.html import format_html
from django.utils.timezone import localtime



# Register your models here.
@admin.register(AttemptCounter)
class AttemptCounterAdmin(admin.ModelAdmin):
    list_display = ('attempts',)

@admin.register(Click)
class ClickAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'formatted_timestamp', 'user_agent')  # Tilføj kolonner til visning
    ordering = ('-timestamp',)  # Sortér efter nyeste klik først
    search_fields = ('ip_address', 'user_agent')  # Gør det muligt at søge
    list_filter = ('timestamp',)  # Tilføj filtre baseret på tid

    def formatted_timestamp(self, obj):
        # Formatér timestamp som fed tekst
        return format_html('<b>{}</b>', localtime(obj.timestamp).strftime('%Y-%m-%d %H:%M:%S'))
    formatted_timestamp.short_description = 'Timestamp'
