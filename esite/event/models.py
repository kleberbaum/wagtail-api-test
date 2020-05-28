from django.http import HttpResponse
from django.db import models
from django.core.validators import RegexValidator
from wagtail.admin.edit_handlers import FieldPanel

from django.contrib.auth import get_user_model

from esite.session.models import Session
from esite.session.widgets import SessionChooser

#from grapple.models import (
#    GraphQLField,
#    GraphQLString,
#    GraphQLStreamfield,
#)

# Create your homepage related models here.

class Event(models.Model):
    event_name = models.CharField(primary_key=True, max_length=16)
    event_scope = models.CharField(null=True, blank=True, max_length=256)
    event_from = models.DateField(null=True, blank=True)
    event_to = models.DateField(null=True, blank=True)
    event_attendees = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(null=False, blank=False, default=True)
    assoc_sessions = models.ForeignKey(Session,
                                   null=True,
                                   blank=False,
                                   on_delete=models.SET_NULL,
                                   related_name='+',
                                   verbose_name="Associated Session")

    panels = [
        FieldPanel('is_active'),
        FieldPanel('event_name'),
        FieldPanel('event_scope'),
        FieldPanel('event_from'),
        FieldPanel('event_to'),
        FieldPanel('event_attendees'),
        FieldPanel('assoc_sessions', widget=SessionChooser),
    ]

    def __str__(self):
        return self.event_name