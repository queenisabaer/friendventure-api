from rest_framework import serializers
from .models import Friendventure


class FriendventureSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_pic = serializers.ReadOnlyField(source="owner.profile.profile_image.url")

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner
    
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
        ]
