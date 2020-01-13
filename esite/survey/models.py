import json
import uuid
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)
from wagtail.core import blocks
from wagtail.core.fields import StreamField, RichTextField
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList, InlinePanel, StreamFieldPanel, MultiFieldPanel, FieldPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField, AbstractFormSubmission
from wagtail.contrib.forms.models import AbstractForm, AbstractFormField, AbstractEmailForm, AbstractFormField, AbstractFormSubmission
from wagtail.admin.utils import send_mail
from esite.user.models import User

# Create your registration related models here.


class FormField(AbstractFormField):
    page = ParentalKey('SurveyFormPage', on_delete=models.CASCADE, related_name='form_fields')

class SurveyFormPage(AbstractEmailForm):
    # When creating a new Form page in Wagtail
    survey_head = models.CharField(null=True, blank=False, max_length=255)
    survey_subhead = RichTextField(null=True, blank=False, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'])

    thank_you_text = RichTextField(null=True, blank=False, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code'])

    content_panels = AbstractEmailForm.content_panels + [
        MultiFieldPanel(
            [
            FieldPanel('survey_head', classname="full title"),
            FieldPanel('survey_subhead', classname="full"),
            FieldPanel('thank_you_text', classname="full"),
            ],
            heading="content",
        ),
        MultiFieldPanel(
            [
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel("subject"),
            ],
            heading="Email Settings"
        ),
        MultiFieldPanel(
            [
                InlinePanel('form_fields', label="Form fields")
            ],
            heading="data",
        )
    ]

    # Called when a user takes part in the survey
    def send_mail(self, form):
        addresses = [x.strip() for x in self.to_address.split(',')]

        emailheader = "New registration via Pharmaziegasse Website"

        content = []
        for field in form:
            value = field.value()
            if isinstance(value, list):
                value = ', '.join(value)
            content.append('{}: {}'.format(field.label, value))
        content = '\n'.join(content)
        
        content += '\n\nMade with ❤ by a tiny SNEK'

        #emailfooter = '<style>@keyframes pulse { 10% { color: red; } }</style><p>Made with <span style="width: 20px; height: 1em; color:#dd0000; animation: pulse 1s infinite;">&#x2764;</span> by <a style="color: lightgrey" href="https://www.aichner-christian.com" target="_blank">Werbeagentur Christian Aichner</a></p>'
        
        #html_message = f"{emailheader}\n\n{content}\n\n{emailfooter}"
        
        send_mail(self.subject, f"{emailheader}\n\n{content}", addresses, self.from_address)
        