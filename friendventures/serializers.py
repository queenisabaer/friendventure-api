from rest_framework import serializers
from .models import Friendventure
from participants.models import Participant
from bookmarks.models import Bookmark
from datetime import datetime


class FriendventureSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_pic = serializers.ReadOnlyField(source="owner.profile.profile_image.url")
    bookmark_id = serializers.SerializerMethodField()
    participants_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_bookmark_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            bookmark = Bookmark.objects.filter(
                owner=user, friendventure=obj
            ).first()
            return bookmark.id if bookmark else None
        return None
    
    def get_participants_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            participant = Participant.objects.filter(
                owner=user, friendventure=obj
            ).first()
            return participant.id if participant else None
        return None
    
    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError("Image can't be larger than 2MB")
        if value.image.width > 2048:
            raise serializers.ValidationError(
                "Image width can't be larger than 2048px"
            )
        if value.image.height > 2048:
            raise serializers.ValidationError(
                "Image height can't be larger than 2048px"
            )
        return value
    
    def validate_date(self, value):
        if value < datetime.now().date():
            raise serializers.ValidationError("The date must be in the future.")
        return value

    class Meta:
        model = Friendventure
        fields = [
            "id",
            "owner",
            "title",
            "image",
            "date",
            "time",
            "place",
            "description",
            "category",
            "created_at",
            "updated_at",
            "is_owner",
            "profile_id",
            "profile_pic",
            "bookmark_id",
            "participants_id",
        ]
        