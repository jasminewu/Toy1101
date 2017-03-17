from rest_framework import serializers
# from app2.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from app2.models import Snippet

#add user api
from django.contrib.auth.models import User

# class SnippetSerializer(serializers.Serializer):
#     # pk = serializers.IntegerField(read_only=True)
#     # title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     # code = serializers.CharField(style={'base_template': 'textarea.html'})
#     # linenos = serializers.BooleanField(required=False)
#     # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES,default='python')
#     # style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#     #
#     # def create(self, validated_data):
#     #     return Snippet.objects.create(**validated_data)
#     #
#     # def update(self, instance, validated_data):
#     #     instance.title = validated_data.get('title', instance.title)
#     #     instance.code = validated_data.get('code', instance.code)
#     #     instance.linenos = validated_data.get('linenos', instance.linenos)
#     #     instance.language = validated_data.get('language', instance.language)
#     #     instance.style = validated_data.get('style', instance.style)
#     #     instance.save()
#     #     return instance

# use  ModelSerializer
class SnippetSerializer(serializers.ModelSerializer):
    #add user api
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ('owner','id', 'title', 'code', 'linenos', 'language','style')


# add user api
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
