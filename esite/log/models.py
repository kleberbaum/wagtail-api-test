from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel, MultiFieldPanel, FieldPanel

#from .blocks import UserChooserBlock
from .widgets import UserChooser


class Workpackage(models.Model):
    STATUS = (
        ('new', 'Workpackage has not been started'),
        ('ongoing', 'Workpackage is in progress'),
        ('waiting', 'Workpackage cannot be continued due to dependencies'),
        ('review', 'Workpackage is under review'),
        ('fin', 'Workpackage is complted and reviewed'),
    )

    name = models.CharField(null=True, blank=False, max_length=255)
    status = models.CharField(
        max_length=32,
        choices=STATUS,
        default='new',
    )
    durration = models.DurationField(null=True, blank=False)
    # OUTDATED
    realtime = models.DurationField(null=True, blank=False, default='00:00:00')
    starttime = models.DateTimeField(null=True, blank=True)
    sid = models.CharField(max_length=3,
                           validators=[
                               RegexValidator(
                                   regex='^\d{3}$',
                                   message='ID doesnt comply',
                               ),
                           ],
                           default="000",
                           unique=True)
    did = models.CharField(max_length=7,
                           validators=[
                               RegexValidator(
                                   regex='^\d{3}\-\d{3}$',
                                   message='ID doesnt comply',
                               ),
                           ],
                           default="000-000")
    pid = models.CharField(max_length=11,
                           validators=[
                               RegexValidator(
                                   regex='^\d{3}\-\d{3}-\d{3}$',
                                   message='ID doesnt comply',
                               ),
                           ],
                           default="000-000-000",
                           primary_key=True)
    start = models.TimeField(null=True, blank=False)
    end = models.TimeField(null=True, blank=False)

    assoc_user = models.ForeignKey(get_user_model(),
                                   null=True,
                                   blank=False,
                                   on_delete=models.SET_NULL,
                                   related_name='+',
                                   verbose_name="Associated User")

    # assoc_user_list = StreamField([
    #     ('userchooser', UserChooserBlock(help_text="A user associated with the workpackage"))
    # ], null=True, blank=True)

    panels = [
        FieldPanel('pid'),
        FieldPanel('did'),
        FieldPanel('sid'),
        FieldPanel('name'),
        FieldPanel('status'),
        FieldPanel('durration'),
        FieldPanel('starttime'),
        FieldPanel('realtime'),
        FieldPanel('assoc_user', widget=UserChooser),
        #StreamFieldPanel(assoc_user_list)
    ]

    def __str__(self):
        return self.name


# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2020 miraculix-org Florian Kleber