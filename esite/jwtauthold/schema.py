from django.contrib.auth import get_user_model

import graphene
import graphql_jwt
from graphene_django import DjangoObjectType
from graphql import GraphQLError

from wagtail.core.models import Page

from esite.user.models import User
from esite.profile.models import ProfilePage
from esite.customer.models import Customer
from esite.registration.schema import UserType

# Create your registration related graphql schemes here.

#class UserType(DjangoObjectType):
#    class Meta:
#        model = User
#        exclude_fields = ['password']

class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(UserType)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)
