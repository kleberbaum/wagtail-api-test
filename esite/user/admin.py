from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

# Register your user related models here.

from .models import User

from esite.customer.admin import CustomerAdmin
from esite.registration.admin import RegistrationAdmin

class UserAdmin(ModelAdmin):
    model = User
    menu_label = "User"
    menu_icon = "user"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
   
    # Listed in the user overview
    list_display = ('date_joined', 'username', 'email')
    search_fields = ('date_joined', 'username', 'email')

#modeladmin_register(UserAdmin)

class CustomerAdminB(ModelAdminGroup):
    menu_label = "User Management"
    menu_icon = "group"
    menu_order = 110
    add_to_settings_menu = False
    exclude_from_explorer = False
    items = (
        UserAdmin,
        CustomerAdmin,
        RegistrationAdmin
    )

modeladmin_register(CustomerAdminB)
