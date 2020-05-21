from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from graphql_jwt.decorators import login_required, permission_required, staff_member_required, superuser_required

# Create your registration related graphql schemes here.
