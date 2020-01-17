
from django.http import HttpResponse
from django.db import models
import django.contrib.auth.validators
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.admin.edit_handlers import PageChooserPanel, TabbedInterface, ObjectList, InlinePanel, StreamFieldPanel, MultiFieldPanel, FieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.forms.models import AbstractForm, AbstractFormField
from modelcluster.fields import ParentalKey

from esite.colorfield.fields import ColorField, ColorAlphaField
from esite.colorfield.blocks import ColorBlock, ColorAlphaBlock, GradientColorBlock

#from grapple.models import (
#    GraphQLField,
#    GraphQLString,
#    GraphQLStreamfield,
#)

# Create your homepage related models here.

class Language(blocks.StructBlock):
    color = blocks.CharBlock(null=True, blank=True, help_text="Bold header text", max_length=80)
    name = blocks.CharBlock(null=True, blank=True, help_text="Bold header text", max_length=80)
    size = blocks.IntegerBlock(null=True, blank=True, help_text="Bold header text")
    share = blocks.IntegerBlock(null=True, blank=True, help_text="Bold header text")

class Languages(blocks.StructBlock):
    total = blocks.IntegerBlock(null=True, blank=True, help_text="Bold header text")
    slices = blocks.StreamBlock([
        ('Language', Language(null=True, blank=True, icon='cogs'))
    ], null=True, blank=True, max_num=8)

class _S_TopLanguages(blocks.StructBlock):
    slices = blocks.StreamBlock([
        ('Language', Language(null=True, blank=True, icon='cogs'))
    ], null=True, blank=True, max_num=8)

class Day(blocks.StructBlock):
    Date = blocks.DateBlock(null=True, blank=True)
    total = blocks.IntegerBlock(null=True, blank=True, help_text="Bold header text")

class Streak(blocks.StructBlock):
    startDate = blocks.DateBlock(null=True, blank=True)
    endDate = blocks.DateBlock(null=True, blank=True)
    total = blocks.IntegerBlock(null=True, blank=True, help_text="Bold header text")

class _S_Calendar(blocks.StructBlock):
    total = blocks.IntegerBlock(null=True, blank=True, help_text="Bold header text")
    busiest_day = Day(null=True, blank=True)
    longest_streak = Streak(null=True, blank=True)
    current_streak = Streak(null=True, blank=True)
    calendar = blocks.TextBlock(null=True, blank=True)

class Contribution(blocks.StructBlock):
    datetime = blocks.DateBlock(null=True, blank=True)
    nameWithOwner = blocks.CharBlock(null=True, blank=True, help_text="Bold header text", max_length=80)
    repoUrl = blocks.CharBlock(null=True, blank=True, help_text="Bold header text", max_length=2048)
    type = blocks.CharBlock(null=True, blank=True, help_text="Bold header text", max_length=80)

class Statistic(blocks.StructBlock):
    year = blocks.IntegerBlock(null=True, blank=True)

class Repository(blocks.StructBlock):
    avatarUrl = blocks.CharBlock(null=True, blank=True, help_text="Bold header text", max_length=2048)
    url = blocks.CharBlock(null=True, blank=True, help_text="Bold header text", max_length=2048)
    name = blocks.CharBlock(null=True, blank=True, help_text="Bold header text", max_length=80)

class Member(blocks.StructBlock):
    avatarUrl = blocks.CharBlock(null=True, blank=True, help_text="Bold header text", max_length=2048)
    url = blocks.CharBlock(null=True, blank=True, help_text="Bold header text", max_length=2048)
    fullname = blocks.CharBlock(null=True, blank=True, help_text="Bold header text", max_length=80)
    username = blocks.CharBlock(null=True, blank=True, help_text="Bold header text", max_length=80)

class Organization(blocks.StructBlock):
    avatarUrl = blocks.CharBlock(null=True, blank=True, help_text="Bold header text", max_length=2048)
    url = blocks.CharBlock(null=True, blank=True, help_text="Bold header text", max_length=2048)
    name = blocks.CharBlock(null=True, blank=True, help_text="Bold header text", max_length=80)
    members = blocks.StreamBlock([
        ('member', Member(null=True, blank=True, icon='cogs'))
    ], null=True, blank=True, max_num=8)

class Platform(blocks.StructBlock):
    sources = models.TextField(null=True, blank=False)
    platformName = blocks.CharBlock(null=True, blank=True, help_text="Bold header text", max_length=80)
    platformUrl = blocks.CharBlock(null=True, blank=True, help_text="Bold header text", max_length=2048)
    avatarUrl = blocks.CharBlock(null=True, blank=True, help_text="Bold header text", max_length=2048)
    websiteUrl = blocks.CharBlock(null=True, blank=True, help_text="Bold header text", max_length=2048)
    company = blocks.CharBlock(null=True, blank=True, help_text="Bold header text", max_length=80)
    email = blocks.CharBlock(null=True, blank=True, help_text="Bold header text", max_length=80)
    username = blocks.CharBlock(null=True, blank=True, help_text="Bold header text", max_length=80)
    fullname = blocks.CharBlock(null=True, blank=True, help_text="Bold header text", max_length=80)
    createdAt = blocks.CharBlock(null=True, blank=True, help_text="Bold header text", max_length=80)
    location = blocks.CharBlock(null=True, blank=True, help_text="Bold header text", max_length=80)
    statusMessage = blocks.CharBlock(null=True, blank=True, help_text="Bold header text", max_length=80)
    statusEmojiHTML = blocks.CharBlock(null=True, blank=True, help_text="Bold header text", max_length=80)


#> Profilepage
class ProfilePage(Page):
    platform_data = models.TextField(null=True, blank=True)
    verified = models.BooleanField(blank=True, default=False)
    available_for_hire = models.BooleanField(blank=True, default=False)
    username = models.CharField(null=True, blank=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 36 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=36, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')
    first_name = models.CharField(null=True, max_length=30, blank=True)
    last_name = models.CharField(null=True, max_length=150, blank=True)
    telephone = models.CharField(null=True, blank=True, max_length=40)
    address = models.CharField(null=True, blank=True, max_length=60)
    postal_code = models.CharField(null=True, blank=True,max_length=12)
    city = models.CharField(null=True, blank=True,max_length=60)
    country = models.CharField(null=True, blank=True, max_length=2)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    company = models.CharField(null=True, blank=True, max_length=80)
    platforms = StreamField([
        ('platform', Platform(null=True, blank=True, icon='fa-instagram')),  
    ], null=True, blank=True)
    organizations = StreamField([
        ('organization', Organization(null=True, blank=True, icon='fa-instagram')),  
    ], null=True, blank=True)
    languages = StreamField([
        ('languages', Languages(null=True, blank=True, icon='fa-instagram')),  
    ], null=True, blank=True)

    main = StreamField([
        ('top_language', _S_TopLanguages(null=True, blank=True, icon='fa-instagram')),  
        ('contribution', Contribution(null=True, blank=True, icon='home')),
        ('code', blocks.RawHTMLBlock(null=True, blank=True, icon='code')),
        ('calendar', _S_Calendar(null=True, blank=True, icon='home')),
    ], null=True, blank=True)


    #graphql_fields = [
    #    GraphQLStreamfield("headers"),
    #    GraphQLStreamfield("sections"),
    #]

    data_panels = [
        FieldPanel('platform_data'),
        FieldPanel('sources'),
    ]

    main_content_panels = [
        MultiFieldPanel(
            [
                FieldPanel('verified'),
                FieldPanel('available_for_hire'),
                FieldPanel('username'),
                FieldPanel('first_name'),
                FieldPanel('last_name'),
                FieldPanel('telephone'),
                FieldPanel('address'),
                FieldPanel('postal_code'),
                FieldPanel('city'),
                FieldPanel('country'),
                FieldPanel('email'),
                FieldPanel('website'),
                FieldPanel('company'),
                StreamFieldPanel('platforms'),
                StreamFieldPanel('organizations'),
                StreamFieldPanel('languages'),
            ],
            heading="aside",
        ),
        StreamFieldPanel('main'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels + main_content_panels, heading='Overview'),
        ObjectList(data_panels + Page.promote_panels + Page.settings_panels, heading='Settings', classname="settings")
    ])
