from django import forms
from django.contrib.auth import validators
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

from generic_chooser.views import ModelChooserViewSet
from django.contrib.auth import get_user_model

from wagtail.admin import widgets


class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'is_customer', 'customer_id', 'telegram_id']

class UserChooserViewSet(ModelChooserViewSet):
    icon = 'pilcrow'
    model = get_user_model()
    page_title = _("Choose a User")
    per_page = 10
    form_class = UserForm

# Create your views here.
