from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
	path('', views.usersignup, name="register_user"),
	#path('activate_account/(<uidb64>[0-9A-Za-z_\-]+)/(<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', views.activate_account, name='activate')
	path('activate_account/<uidb64>/<token>', views.activate_account, name='activate')

]