from django.http import HttpResponse
from django.db import models
from django.core.validators import RegexValidator
from wagtail.admin.edit_handlers import FieldPanel

#from grapple.models import (
#    GraphQLField,
#    GraphQLString,
#    GraphQLStreamfield,
#)

# Create your homepage related models here.

class Session(models.Model):
    session_token = models.CharField(primary_key=True, max_length=16)
    session_name = models.CharField(null=True, blank=True, max_length=16)
    session_scope = models.CharField(null=True, blank=True, max_length=256)
    session_from = models.DateField(null=True, blank=True)
    session_to = models.DateField(null=True, blank=True)
    session_room = models.CharField(null=True, blank=True, max_length=16)
    
    panels = [
        FieldPanel('session_token'),
        FieldPanel('session_name'),
        FieldPanel('session_scope'),
        FieldPanel('session_from'),
        FieldPanel('session_to'),
        FieldPanel('session_room')
    ]

    def __str__(self):
        return self.session_token
