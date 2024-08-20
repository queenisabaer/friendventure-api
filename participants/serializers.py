from rest_framework import serializers
from .models import Participant
from django.db import IntegrityError


class ParticipantSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Participant
        fields = [
            'id',
            'owner',
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
