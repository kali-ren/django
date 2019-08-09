from django.shortcuts import render
from rest_framework import viewsets
from .models import Messages
from .serializers import mySerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class MessageViewSet(viewsets.ModelViewSet):
	permissions_classes = (IsAuthenticated,)
	queryset 		    = Messages.objects.all() 
	serializer_class    = mySerializer
	
