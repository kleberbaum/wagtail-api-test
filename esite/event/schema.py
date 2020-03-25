from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError

from .models import Event
# Create your user related graphql schemes here.


class Query(graphene.ObjectType):
    events = graphene.List(EventType)

    def resolve_events(self, info):
        # To list all events
        return Event.objects.all()

