from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from graphql_jwt.decorators import login_required, permission_required, staff_member_required, superuser_required

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


class CacheUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        token = graphene.String(required=False)
        platform_data = graphene.String(required=True)

    @login_required
    def mutate(self, info, token, platform_data):
        user = info.context.user

        #user.platform_data = platform_data
        #user.save()

        profile_page = Page.objects.get(slug=f"{user.username}").specific

        profile_page.platform_data = platform_data

        profile_page.save_revision().publish()

        return CacheUser(user=user)

class CacheUserByName(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        token = graphene.String(required=False)
        username = graphene.String(required=False)
        platform_data = graphene.String(required=True)

    @login_required
    def mutate(self, info, token, username, platform_data):
        user = info.context.user

        profile_page = Page.objects.get(slug=f"{username}").specific

        profile_page.platform_data = platform_data

        profile_page.save_revision().publish()

        return CacheUser(user=user)