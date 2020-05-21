from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

# Register your registration related models here.

from .models import Registration

class RegistrationAdmin(ModelAdmin):
    model = Registration
    menu_label = "Registration"
    menu_icon = "mail"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False

    # Listed in the registration overview
    list_display = ('date_joined', 'title', 'first_name', 'last_name', 'email', 'telephone', 'address', 'postal_code', 'city', 'country', 'newsletter')
    search_fields = ('date_joined', 'title', 'first_name', 'last_name', 'email', 'telephone', 'address', 'postal_code', 'city', 'country', 'newsletter')

#modeladmin_register(RegistrationAdmin)
