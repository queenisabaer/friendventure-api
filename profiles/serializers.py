from rest_framework import serializers
from .models import Profile
from followers.models import Follower

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    participates_count = serializers.ReadOnlyField()
    friendventures_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
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

    class Meta:
        model = Profile
        fields = [
            'id',
            'owner',
            'name',
            'profile_image',
            'description',
            'phone_number',
            'email',
            'created_at',
            'updated_at',
            'is_owner',
            'following_id',
            'followers_count',
            'following_count',
            'participates_count',
            'friendventures_count',
        ]