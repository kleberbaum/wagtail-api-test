from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register


# Register your registration related models here.

from .models import Event
from esite.session.admin import SessionAdmin

class EventAdmin(ModelAdmin):
    model = Event
    menu_label = "Event"
    menu_icon = "mail"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False

    # Listed in the registration overview
    list_filter = ('is_active','event_name')
    list_display = ('is_active', 'event_name', 'event_scope', 'event_from', 'event_to', 'event_attendees')
    search_fields = ('is_active', 'event_name', 'event_scope', 'event_from', 'event_to', 'event_attendees')

#modeladmin_register(UserAdmin)

class LogAdmin(ModelAdminGroup):
    menu_label = "Event Management"
    menu_icon = "group"
    menu_order = 110
    add_to_settings_menu = False
    exclude_from_explorer = False
    items = (
        EventAdmin,
        SessionAdmin,
    )

modeladmin_register(LogAdmin)