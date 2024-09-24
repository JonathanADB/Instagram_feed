from rest_framework import serializers
from .models import *

class InstagramMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramMedia
        fields = ['media_type', 'media_url']
        read_only_fields = ['media_type', 'media_url']

class InstagramPostSerializer(serializers.ModelSerializer):
    media = InstagramMediaSerializer(many=True)

    class Meta:
        model = InstagramPost
        fields = ['post_id', 'description', 'timestamp', 'media']
        read_only_fields = ['post_id', 'description', 'timestamp', 'media']

class InstagramAccountSerializer(serializers.ModelSerializer):
    posts = InstagramPostSerializer(many=True, source='instagrampost_set', read_only=True)
    profile_pic_url = serializers.ImageField(read_only=True)

    class Meta:
        model = InstagramAccount
        fields = ['username', 'last_updated', 'profile_pic_url', 'posts']
        read_only_fields = ['username', 'last_updated', 'profile_pic_url', 'posts']
