from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

# Register your user related models here.

from .models import Workpackage

from esite.customer.admin import CustomerAdmin
from esite.registration.admin import RegistrationAdmin

class WorkpackageAdmin(ModelAdmin):
    model = Workpackage
    menu_label = "Workpackage"
    menu_icon = "user"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    # Listed in the user overview
    list_display = ( 'pid', 'did', 'sid', 'name', 'status', 'durration', 'realtime', 'assoc_user')
    list_filter = ('status','assoc_user')
    search_fields = ( 'pid', 'did', 'sid', 'name', 'status', 'durration', 'realtime', 'assoc_user')

#modeladmin_register(UserAdmin)

class LogAdmin(ModelAdminGroup):
    menu_label = "Snek Management"
    menu_icon = "group"
    menu_order = 110
    add_to_settings_menu = False
    exclude_from_explorer = False
    items = (
        WorkpackageAdmin,
    )

modeladmin_register(LogAdmin)
