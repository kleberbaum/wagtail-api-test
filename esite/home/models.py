from django.http import HttpResponse
from django.db import models
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

from esite.api.helpers import register_streamfield_block

from esite.api.models import (
    GraphQLForeignKey,
    GraphQLField,
    GraphQLStreamfield,
    GraphQLImage,
    GraphQLString,
    GraphQLCollection,
    GraphQLEmbed,
    GraphQLSnippet,
)

# Create your homepage related models here.

@register_snippet
class Button(models.Model):
    button_title = models.CharField(null=True, blank=False, max_length=255)
    button_embed = models.CharField(null=True, blank=True, max_length=255)
    button_link = models.URLField(null=True, blank=True)
    button_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    panels = [
        FieldPanel('button_title'),
        FieldPanel('button_embed'),
        FieldPanel('button_link'),
        PageChooserPanel('button_page')
    ]

    def __str__(self):
        return self.button_title


#> Header
@register_streamfield_block
class _H_HeroBlock(blocks.StructBlock):
    slide_image = ImageChooserBlock(null=True, blank=False, help_text="Big, high resolution slider image")
    slide_button = SnippetChooserBlock(Button, null=True, blank=True, required=False, help_text="The button displayed at the frontpage slider")

    graphql_fields = [GraphQLImage("slide_image"), GraphQLSnippet("slide_button", "home.Button")]

#> Why Section
@register_streamfield_block
class Why_ColumnBlock(blocks.StructBlock):
    Column_image = ImageChooserBlock(null=True, blank=False, help_text="Icon representating the below content")
    Column_head = blocks.CharBlock(null=True, blank=False, classname="full title", help_text="The bold header text at the frontpage slider")
    Column_subhead = blocks.RichTextBlock(null=True, blank=False, help_text="The content of the frontpage slider element", classname="full")
    Column_paragraph = blocks.RichTextBlock(null=True, blank=False, help_text="Formatted text", classname="full")

@register_streamfield_block
class _S_WhyBlock(blocks.StructBlock):
    why_head = blocks.CharBlock(null=True, blank=False, classname="full title", help_text="Bold header text")
    why_displayhead = blocks.BooleanBlock(null=True, blank=True, default=True, required=False, help_text="Whether or not to display the header")
    why_Columns = blocks.StreamBlock([
        ('why_Column', Why_ColumnBlock(null=True, blank=False, icon='cogs'))
    ], null=True, blank=False, max_num=8)

#> About Shop
@register_streamfield_block
class Shop_PricingcardBlock(blocks.StructBlock):
    shopcard_background = ColorBlock(null=True, blank=False, help_text="Select background color that contrasts text")
    shopcard_title = blocks.CharBlock(null=True, blank=False, classname="full title", help_text="Title of pricing card")
    shopcard_description = blocks.RichTextBlock(null=True, blank=False, help_text="Description of offer", classname="full")
    shopcard_price = blocks.DecimalBlock(null=True, blank=False, decimal_places=2, help="Price of the offer")
    shopcard_sucessmsg = blocks.RichTextBlock(null=True, blank=False, help_text="Success message", classname="full")
    shopcard_button = SnippetChooserBlock(Button, null=True, blank=True, required=False, help_text="Button displayed at the pricing-section")

@register_streamfield_block
class _S_ShopBlock(blocks.StructBlock):
    #shop_background = ColorBlock(null=True, blank=False, help_text="Select background color that contrasts text")
    shop_head = blocks.CharBlock(null=True, blank=False, classname="full title", help_text="Bold header text")
    shop_displayhead = blocks.BooleanBlock(null=True, blank=True, default=True, required=False, help_text="Whether or not to display the header")

#> About Section
@register_streamfield_block
class About_CardBlock(blocks.StructBlock):
    card_image = ImageChooserBlock(null=True, blank=False, help_text="Office-fitting image")
    card_head = blocks.CharBlock(null=True, blank=False, classname="full title", help_text="The bold header text at the frontpage slider")
    card_paragraph = blocks.RichTextBlock(null=True, blank=False, help_text="Formatted text", classname="full")

@register_streamfield_block
class _S_AboutBlock(blocks.StructBlock):
    about_head = blocks.CharBlock(null=True, blank=False, classname="full title", help_text="Bold header text")
    about_displayhead = blocks.BooleanBlock(null=True, blank=True, default=True, required=False, help_text="Whether or not to display the header")
    about_cards = blocks.StreamBlock([
        ('aboutcard', About_CardBlock(null=True, blank=False, icon='cogs'))
    ], null=True, blank=False, max_num=6)

#> Instagram Section
@register_streamfield_block
class _S_InstagramBlock(blocks.StructBlock):
    instagram_id = blocks.CharBlock(null=True, blank=False, classname="full", help_text="Instagram-Account id")
    instagram_pc = blocks.CharBlock(null=True, blank=False, classname="full", help_text="Instagram-Post count")

#> Steps Section
@register_streamfield_block
class Steps_StepBlock(blocks.StructBlock):
    step_image = ImageChooserBlock(null=True, blank=False, help_text="Image fitting this step")
    step_head = blocks.CharBlock(null=True, blank=False, classname="full title", help_text="Bold header text")
    step_subhead = blocks.RichTextBlock(null=True, blank=False, help_text="Short introduction to the following paragraph", classname="full")
    step_paragraph = blocks.RichTextBlock(null=True, blank=False, help_text="Step paragraph", classname="full")

@register_streamfield_block
class _S_StepsBlock(blocks.StructBlock):
    steps_head = blocks.CharBlock(null=True, blank=False, classname="full title", help_text="Bold header text")
    steps_displayhead = blocks.BooleanBlock(null=True, blank=True, default=True, required=False, help_text="Whether or not to display the header")
    steps_steps = blocks.StreamBlock([
        ('step', Steps_StepBlock(null=True, blank=False))
    ], null=True, blank=False, max_num=4)

#> Trusted Section
@register_streamfield_block
class Trusted_PartnerBlock(blocks.StructBlock):
    partner_logo = ImageChooserBlock(null=True, blank=False, help_text="Image fitting this step")
    partner_link = blocks.URLBlock(null=True, blank=True, help_text="Important! Format https://www.domain.tld/xyz")

@register_streamfield_block
class _S_TrustedBlock(blocks.StructBlock):
    trusted_partner = blocks.StreamBlock([
        ('partner', Trusted_PartnerBlock(null=True, blank=False))
    ], null=True, blank=False, max_num=4)

#> Instagram Section
@register_streamfield_block
class _S_WolfBlock(blocks.StructBlock):
    wolf_head = blocks.CharBlock(null=True, blank=False, classname="full", help_text="Bold header text")
    wolf_subhead = blocks.RichTextBlock(null=True, blank=False, help_text="The content of the black wolf coffee intro", classname="full")

#> Trusted Section
@register_streamfield_block
class FAQ_QuestionBlock(blocks.StructBlock):
    question_icon = blocks.CharBlock(null=True, blank=True, help_text="Font Awesome icon name (e.g. facebook-f) from https://fontawesome.com/icons?d=gallery&s=solid&m=free")
    question_head = blocks.CharBlock(null=True, blank=False, classname="full title", help_text="Bold header text")
    question_paragraph = blocks.RichTextBlock(null=True, blank=False, help_text="Formatted text", classname="full")
    question_link = blocks.URLBlock(null=True, blank=True, help_text="Important! Format https://www.domain.tld/xyz")

@register_streamfield_block
class _S_FAQBlock(blocks.StructBlock):
    header = blocks.CharBlock(null=True, blank=False, classname="full title", help_text="Bold header text")
    questions = blocks.StreamBlock([
        ('question', FAQ_QuestionBlock(null=True, blank=False))
    ], null=True, blank=False, max_num=4)

#> Homepage
class HomePage(Page):
    city = models.CharField(null=True, blank=False, max_length=255)
    zip_code = models.CharField(null=True, blank=False, max_length=255)
    address = models.CharField(null=True, blank=False, max_length=255)
    telephone = models.CharField(null=True, blank=False, max_length=255)
    telefax = models.CharField(null=True, blank=False, max_length=255)
    vat_number = models.CharField(null=True, blank=False, max_length=255)
    whatsapp_telephone = models.CharField(null=True, blank=True, max_length=255)
    whatsapp_contactline = models.CharField(null=True, blank=True, max_length=255)
    tax_id = models.CharField(null=True, blank=False, max_length=255)
    trade_register_number = models.CharField(null=True, blank=False, max_length=255)
    court_of_registry = models.CharField(null=True, blank=False, max_length=255)
    place_of_registry = models.CharField(null=True, blank=False, max_length=255)
    trade_register_number = models.CharField(null=True, blank=False, max_length=255)
    ownership = models.CharField(null=True, blank=False, max_length=255)
    email = models.CharField(null=True, blank=False, max_length=255)

    copyrightholder = models.CharField(null=True, blank=False, max_length=255)

    about = RichTextField(null=True, blank=False)
    privacy = RichTextField(null=True, blank=False)

    sociallinks = StreamField([
        ('link', blocks.URLBlock(help_text="Important! Format https://www.domain.tld/xyz"))
    ])

    array = []
    def sociallink_company(self):
        for link in self.sociallinks:
            self.array.append(str(link).split(".")[1])
        return self.array


    headers = StreamField([
        ('h_hero', _H_HeroBlock(null=True, blank=False, icon='image')),
        ('code', blocks.RawHTMLBlock(null=True, blank=True, classname="full", icon='code'))
    ], null=True, blank=False)

    sections = StreamField([
        ('s_why', _S_WhyBlock(null=True, blank=False, icon='group')),
        ('s_about', _S_AboutBlock(null=True, blank=False, icon='fa-quote-left')),
        ('s_instagram', _S_InstagramBlock(null=True, blank=False, icon='fa-instagram')),
        ('s_steps', _S_StepsBlock(null=True, blank=False, icon='fa-list-ul')),
        ('s_shop', _S_ShopBlock(null=True, blank=False, icon='home')),
        ('s_trusted', _S_TrustedBlock(null=True, blank=False, icon='fa-list-ul')),
        ('s_wolf', _S_WolfBlock(null=True, blank=False, icon='fa-list-ul')),
        ('s_faq', _S_FAQBlock(null=True, blank=False, icon='home')),
        ('code', blocks.RawHTMLBlock(null=True, blank=True, classname="full", icon='code'))
    ], null=True, blank=False)

    token = models.CharField(null=True, blank=True, max_length=255)

    graphql_fields = [
        GraphQLStreamfield("headers"),
        GraphQLStreamfield("sections"),
    ]

    main_content_panels = [
        StreamFieldPanel('headers'),
        StreamFieldPanel('sections')
    ]

    imprint_panels = [
        MultiFieldPanel(
            [
            FieldPanel('city'),
            FieldPanel('zip_code'),
            FieldPanel('address'),
            FieldPanel('telephone'),
            FieldPanel('telefax'),
            FieldPanel('whatsapp_telephone'),
            FieldPanel('whatsapp_contactline'),
            FieldPanel('email'),
            FieldPanel('copyrightholder')
            ],
            heading="contact",
        ),
        MultiFieldPanel(
            [
            FieldPanel('vat_number'),
            FieldPanel('tax_id'),
            FieldPanel('trade_register_number'),
            FieldPanel('court_of_registry'),
            FieldPanel('place_of_registry'),
            FieldPanel('trade_register_number'),
            FieldPanel('ownership')
            ],
            heading="legal",
        ),
        StreamFieldPanel('sociallinks'),
        MultiFieldPanel(
            [
            FieldPanel('about'),
            FieldPanel('privacy')
            ],
            heading="privacy",
        )
    ]

    token_panel = [
        FieldPanel('token')
    ]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels + main_content_panels, heading='Main'),
        ObjectList(imprint_panels, heading='Imprint'),
        ObjectList(Page.promote_panels + token_panel + Page.settings_panels, heading='Settings', classname="settings")
    ])
