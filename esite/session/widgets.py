from django.contrib.admin.utils import quote
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from generic_chooser.widgets import AdminChooser
from .models import Session


class SessionChooser(AdminChooser):
    choose_one_text = _('Choose a Session')
    model = Session
    choose_modal_url_name = 'session_chooser:choose'