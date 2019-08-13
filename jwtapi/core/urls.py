from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RoleViewSet
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('roles', RoleViewSet)

app_name = 'core'
urlpatterns = [
	path('', include(routers.urls)),
	path('api-auth/', include('rest_framework.urls')),
	path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]