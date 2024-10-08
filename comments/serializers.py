from rest_framework import serializers
from .models import Comment
from django.contrib.humanize.templatetags.humanize import naturaltime


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.

    Includes fields for the comment's owner, profile details, and timestamps,
    as well as custom fields for checking ownership and formatting dates.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_pic = serializers.ReadOnlyField(
        source='owner.profile.profile_image.url'
    )
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Comment
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_pic',
            'created_at',
            'updated_at',
            'friendventure',
            'content'
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for detailed view of the Comment model, inheriting from CommentSerializer.

    Adds the friendventure ID as a read-only field.
    """
    friendventure = serializers.ReadOnlyField(source='friendventure.id')
