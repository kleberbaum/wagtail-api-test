from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

# Register your registration related models here.

from .models import Event

class EventAdmin(ModelAdmin):
    model = Event
    menu_label = "Event"
    menu_icon = "mail"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False

    # Listed in the registration overview
    list_display = ('is_active', 'event_name', 'event_scope', 'event_from', 'event_to', 'event_attendees')
    search_fields = ('is_active', 'event_name', 'event_scope', 'event_from', 'event_to', 'event_attendees')

modeladmin_register(EventAdmin)
