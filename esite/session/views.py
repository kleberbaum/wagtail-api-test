from django import forms
from django.contrib.auth import validators
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

from generic_chooser.views import ModelChooserViewSet
from .models import Session

from wagtail.admin import widgets


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['session_token', 'session_name', 'session_scope', 'session_from', 'session_to', 'session_room']

class SessionChooserViewSet(ModelChooserViewSet):
    icon = 'pilcrow'
    model = Session
    page_title = _("Choose a Session")
    per_page = 10
    form_class = SessionForm

# Create your views here.
