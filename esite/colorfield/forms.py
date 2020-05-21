#!/usr/bin/env python

import re

from django import forms
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from .widgets import ColorWidget, ColorAlphaWidget, GradientColorWidget

color_re = re.compile('^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')
validate_color = RegexValidator(color_re, _('Enter a valid color.'), 'invalid')

#color_reg = re.compile('^to\s?(\bbottom|\bright|\btop left|\btop right|\btop)\s#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')
#validate_colorg = RegexValidator(color_reg, _('Enter a valid gradient color.'), 'invalid')


class ColorField(forms.CharField):
    default_validators = [validate_color]
    widget = ColorWidget

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 18
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = self.ColorWidget
        return super(ColorField, self).formfield(**kwargs)

    def prepare_value(self, value):
        if isinstance(value, str):
            return value
        # return str(value)
        # or should it be
        return self.prepare_value(str(value))


class ColorAlphaField(forms.CharField):
    #default_validators = [validate_color]
    widget = ColorAlphaWidget

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 18
        super(ColorAlphaField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = self.ColorWidget2
        return super(ColorAlphaField, self).formfield(**kwargs)

    def prepare_value(self, value):
        if isinstance(value, str):
            return value
        # return str(value)
        # or should it be
        return self.prepare_value(str(value))


class GradientColorField(forms.CharField):
    #default_validators = [validate_colorg]
    widget = GradientColorWidget

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 100
        super(GradientColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = self.GradientColorWidget
        return super(GradientColorField, self).formfield(**kwargs)

    def prepare_value(self, value):
        if isinstance(value, str):
            return value
        # return str(value)
        # or should it be
        return self.prepare_value(str(value))

