from django.shortcuts import render
from rest_framework import viewsets
from .models import Role
from .serializers import RoleSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class RoleViewSet(viewsets.ModelViewSet):
	permissions_class = (IsAuthenticated,)
	queryset		  = Role.objects.all()
	serializer_class  = RoleSerializer