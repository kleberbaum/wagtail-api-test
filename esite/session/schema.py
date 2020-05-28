from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError

from .models import Session

# Create your user related graphql schemes here.

class SessionType(DjangoObjectType):
    class Meta:
        model = Session
        #exclude_fields = ['password']


class Query(graphene.ObjectType):
    events = graphene.List(SessionType)

    def resolve_events(self, info):
        # To list all events
        return Session.objects.all()

