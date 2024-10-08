from rest_framework import serializers
from .models import Follower
from django.db import IntegrityError


class FollowerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Follower model.

    Handles serialization of follower relationships, including the owner and the followed user.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = [
            'id',
            'owner',
            'followed_name',
            'followed',
            'created_at'
        ]

    def create(self, validated_data):
        """
        Create a new follower relationship, ensuring the owner and followed are not the same user.
        """
        owner = validated_data.get('owner')
        followed = validated_data.get('followed')

        # Check if owner and followed refer to the same user
        if owner == followed:
            raise serializers.ValidationError({
                'detail': "You cannot follow yourself!"
            })
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'You are already following this user!'
            })
