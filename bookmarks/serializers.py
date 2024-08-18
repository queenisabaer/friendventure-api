from rest_framework import serializers
from .models import Bookmark
from django.db import IntegrityError


class BookmarkSerializer(serializers.ModelSerializer):
    """
    Serializer for the Bookmark model
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Bookmark
        fields = ['id', 'created_at', 'owner', 'friendventure']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'You have already bookmarked this friendventure.'
            })