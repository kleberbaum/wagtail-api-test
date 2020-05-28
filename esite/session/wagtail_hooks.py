import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler
from wagtail.core import hooks
from .views import SessionChooserViewSet



@hooks.register('register_admin_viewset')
def register_session_chooser_viewset():
    return SessionChooserViewSet('session_chooser', url_prefix='session-chooser')