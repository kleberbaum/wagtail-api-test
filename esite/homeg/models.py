from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField
from wagtail.contrib.settings.models import BaseSetting, register_setting

from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.snippets.models import register_snippet
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel

from wagtail_headless_preview.models import HeadlessPreviewMixin
from wagtailmedia.edit_handlers import MediaChooserPanel

from grapple.models import (
    GraphQLField,
    GraphQLString,
    GraphQLSnippet,
    GraphQLStreamfield,
    GraphQLForeignKey,
    GraphQLImage,
    GraphQLDocument,
    GraphQLMedia,
    GraphQLCollection,
    GraphQLPage
)
from .blocks import StreamFieldBlock


class HomePage(Page):
    pass


class AuthorPage(Page):
    name = models.CharField(max_length=255)

    content_panels = Page.content_panels + [
        FieldPanel("name"),
    ]

    graphql_fields = [
        GraphQLString("name"),
    ]


class BlogPage(HeadlessPreviewMixin, Page):
    date = models.DateField("Post date")
    advert = models.ForeignKey(
        "home.Advert",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    cover = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    book_file = models.ForeignKey(
        "wagtaildocs.Document",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    featured_media = models.ForeignKey(
        "wagtailmedia.Media",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    author = models.ForeignKey(
        AuthorPage,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    body = StreamField(StreamFieldBlock())

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        ImageChooserPanel("cover"),
        StreamFieldPanel("body"),
        InlinePanel("related_links", label="Related links"),
        InlinePanel("authors", label="Authors"),
        FieldPanel("author"),
        SnippetChooserPanel("advert"),
        DocumentChooserPanel("book_file"),
        MediaChooserPanel("featured_media"),
    ]

    @property
    def copy(self):
        return self

    graphql_fields = [
        GraphQLString("heading"),
        GraphQLString("date"),
        GraphQLStreamfield("body"),
        GraphQLCollection(
            GraphQLForeignKey, "related_links", "home.blogpagerelatedlink"
        ),
        GraphQLCollection(GraphQLString, "related_urls", source="related_links.url"),
        GraphQLCollection(GraphQLString, "authors", source="authors.person.name"),
        GraphQLSnippet("advert", "home.Advert"),
        GraphQLImage("cover"),
        GraphQLDocument("book_file"),
        GraphQLMedia("featured_media"),
        GraphQLForeignKey("copy", "home.BlogPage"),
        GraphQLPage("author"),
    ]


class BlogPageRelatedLink(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name="related_links")
    name = models.CharField(max_length=255)
    url = models.URLField()

    panels = [FieldPanel("name"), FieldPanel("url")]

    graphql_fields = [GraphQLString("name"), GraphQLString("url")]


@register_snippet
class Person(models.Model):
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    panels = [FieldPanel("name"), FieldPanel("job")]

    graphql_fields = [GraphQLString("name"), GraphQLString("job")]


class Author(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name="authors")
    role = models.CharField(max_length=255)
    person = models.ForeignKey(
        Person, null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )

    panels = [FieldPanel("role"), SnippetChooserPanel("person")]

    graphql_fields = [GraphQLString("role"), GraphQLForeignKey("person", Person)]


@register_snippet
class Advert(models.Model):
    url = models.URLField(null=True, blank=True)
    text = models.CharField(max_length=255)

    panels = [FieldPanel("url"), FieldPanel("text")]

    graphql_fields = [GraphQLString("url"), GraphQLString("text")]

    def __str__(self):
        return self.text


@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(help_text="Your Facebook page URL")
    instagram = models.CharField(
        max_length=255, help_text="Your Instagram username, without the @"
    )
    trip_advisor = models.URLField(help_text="Your Trip Advisor page URL")
    youtube = models.URLField(help_text="Your YouTube channel or user account URL")

    graphql_fields = [
        GraphQLString("facebook"),
        GraphQLString("instagram"),
        GraphQLString("trip_advisor"),
        GraphQLString("youtube"),
    ]
