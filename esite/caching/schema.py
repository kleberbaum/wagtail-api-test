from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from graphql_jwt.decorators import login_required, permission_required, staff_member_required, superuser_required

from esite.user.models import User
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

        user.platform_data = platform_data

        user.save()

        return CacheUser(user=user)

class Mutation(graphene.ObjectType):
    cache_user = CacheUser.Field()
