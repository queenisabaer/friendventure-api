from rest_framework import serializers
from .models import Participant
from django.db import IntegrityError


class ParticipantSerializer(serializers.ModelSerializer):
    """
    Serializer for the Participant model.

    Handles serialization of participant details in a friendventure, including the owner of
    the participant relationship and the associated friendventure.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Participant
        fields = [
            'id',
            'owner',
            'owner_id',
            'friendventure',
            'created_at'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'You are already taking part in this friendventure.'
            })
