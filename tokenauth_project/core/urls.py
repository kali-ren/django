from rest_framework import routers
from . import views
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

routers = routers.DefaultRouter()
routers.register('messages', views.MessageViewSet)

urlpatterns =[
	path('',include(routers.urls)),
	path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]