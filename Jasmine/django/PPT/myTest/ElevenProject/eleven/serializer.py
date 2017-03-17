
from rest_framework import serializers
from django.contrib.auth.models import User
from eleven.models import Moment

class UserSerializer(serializers.ModelSerializer):
    # message = serializers.PrimaryKeyRelatedField(many=True, queryset=Moment.objects.all())
    # photo = serializers.PrimaryKeyRelatedField(many=True, queryset=Moment.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username')

class MomentSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.username')
    class Meta:
        model = Moment
        fields = ( 'id', 'message', 'photo', 'user_id' )
