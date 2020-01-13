import json
import uuid
import django.contrib.auth.validators
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.serializers.json import DjangoJSONEncoder
from django.core.mail import send_mail
from django.db import models
from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)
from wagtail.core.fields import StreamField, RichTextField
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList, InlinePanel, StreamFieldPanel, MultiFieldPanel, FieldPanel

# extend AbstractUser Model from django.contrib.auth.models
class User(AbstractUser):
  # AbstractUser.username field (modified max_length)
  username = models.CharField(null=True, blank=False, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 36 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=36, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')
  is_customer = models.BooleanField(blank=False, default=False)
  customer_id = models.CharField(null=True, blank=True, max_length=36)
  birthdate = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=False)
  telephone = models.CharField(null=True, blank=False, max_length=40)
  address = models.CharField(null=True, blank=True, max_length=60)
  city = models.CharField(null=True, blank=True,max_length=60)
  postal_code = models.CharField(null=True, blank=True,max_length=12)
  country = models.CharField(null=True, blank=True, max_length=2)
  newsletter = models.BooleanField(blank=False, default=False)
  registration_data = models.TextField(null=True, blank=False)
  platform_data = models.TextField(null=True, blank=False)
  education_data = models.TextField(null=True, blank=False)
  sources = models.TextField(null=True, blank=False)
  verified = models.BooleanField(blank=False, default=False)

  # custom save function
  def save(self, *args, **kwargs):
    if not self.username:
      self.username = str(uuid.uuid4())

    if not self.registration_data or self.is_customer:
      if not self.is_active:
        self.is_active = True

        send_mail(
          'got activated',
          'You got activated.',
          'noreply@snek.at',
          [self.email],
          fail_silently=False,
        )


    else:
      self.is_active = False

    super(User, self).save(*args, **kwargs)

  #panels = [
  #  FieldPanel('is_customer'),
  #  FieldPanel('date_joined'),
  #  FieldPanel('title'),
  #  FieldPanel('first_name'),
  #  FieldPanel('last_name'),
  #  FieldPanel('email'),
  #  FieldPanel('telephone'),
  #  FieldPanel('address'),
  #  FieldPanel('postal_code'),
  #  FieldPanel('city'),
  #  FieldPanel('country'),
  #  FieldPanel('newsletter'),
  #  FieldPanel('registration_data'),
  #]

  def __str__(self):
    return self.username
