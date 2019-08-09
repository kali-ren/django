from rest_framework import serializers
from .models import Messages


class mySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model  = Messages
		fields = ['id','message']