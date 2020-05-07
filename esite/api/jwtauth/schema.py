from django.contrib.auth import get_user_model
from wagtail.core.models import Page as wagtailPage
from wagtail.images.models import Image as wagtailImage

import graphene
import graphql_jwt
from graphene_django import DjangoObjectType
from graphql import GraphQLError
import graphene_django_optimizer as gql_optimizer
from graphql.execution.base import ResolveInfo
from ..types.pages import Page
from ..types.images import ImageObjectType as Image

from esite.api.permissions import with_page_permissions, with_collection_permissions

# Create your registration related graphql schemes here.

#class UserType(DjangoObjectType):
#    class Meta:
#        model = User
#        exclude_fields = ['password']

class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):

    profile = graphene.Field(Page)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        user = info.context.user
        profilequery = wagtailPage.objects.filter(slug=f"{user.username}")
        return cls(profile=with_page_permissions(info.context, profilequery.specific()).live().first())
