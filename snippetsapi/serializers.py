
from .models import Snippet,STYLE_CHOICES,LANGUAGE_CHOICES
from rest_framework import serializers
from django.contrib.auth.models import User




class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner=serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    class Meta:
        model = Snippet
        fields = ['owner','url', 'highlight','id', 'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets=serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)


    class Meta:
        model=User
        fields=['url','id','username','snippets']
