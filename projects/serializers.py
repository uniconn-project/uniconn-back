from profiles.serializers import ProfileSerializer03, ProfileSerializer04
from rest_framework import serializers

from .models import (
    Discussion,
    DiscussionReply,
    DiscussionStar,
    Link,
    Market,
    Project,
    ProjectEnteringRequest,
)


class MarketSerializer01(serializers.ModelSerializer):
    """
    Market serializer that serializes only the *id* and *name* of a given market object.
    """

    class Meta:
        model = Market
        fields = ["id", "name"]


class LinksSerializer01(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ["id", "name", "href", "is_public"]


class ProjectStarSerializer01(serializers.ModelSerializer):
    profile = ProfileSerializer03()

    class Meta:
        model = DiscussionStar
        fields = ["id", "profile"]


class ProjectSerializer01(serializers.ModelSerializer):
    """
    Light project serializer - useful for projects list items
    """

    category = serializers.DictField(source="category_value_and_readable")
    students = ProfileSerializer03(source="students_profiles", many=True)
    markets = MarketSerializer01(many=True)
    stars = ProjectStarSerializer01(many=True)

    class Meta:
        model = Project
        fields = ["id", "category", "name", "slogan", "image", "students", "markets", "stars", "discussions_length"]


class ProjectSerializer02(serializers.ModelSerializer):
    """
    Heavy project serializer - useful for project page
    """

    category = serializers.DictField(source="category_value_and_readable")
    students = ProfileSerializer03(source="students_profiles", many=True)
    mentors = ProfileSerializer03(source="mentors_profiles", many=True)
    pending_invited_students = ProfileSerializer03(source="pending_invited_students_profiles", many=True)
    pending_invited_mentors = ProfileSerializer03(source="pending_invited_mentors_profiles", many=True)
    markets = MarketSerializer01(many=True)
    links = LinksSerializer01(many=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "category",
            "name",
            "slogan",
            "image",
            "description",
            "students",
            "mentors",
            "pending_invited_students",
            "pending_invited_mentors",
            "markets",
            "links",
            "stars",
            "discussions_length",
        ]


class ProjectSerializer03(serializers.ModelSerializer):
    """
    Lightest project serializer - only id, name and image
    """

    class Meta:
        model = Project
        fields = ["id", "name", "image"]


class ProjectEnteringRequestSerializer01(serializers.ModelSerializer):
    project = ProjectSerializer03()
    profile = ProfileSerializer04()

    class Meta:
        model = ProjectEnteringRequest
        fields = ["id", "message", "project", "profile"]


class DiscussionStarSerializer01(serializers.ModelSerializer):
    profile = ProfileSerializer03()

    class Meta:
        model = DiscussionStar
        fields = ["id", "profile"]


class DiscussionReplySerializer01(serializers.ModelSerializer):
    profile = ProfileSerializer03()

    class Meta:
        model = DiscussionReply
        fields = ["id", "profile", "content", "created_at"]


class DiscussionSerializer01(serializers.ModelSerializer):
    profile = ProfileSerializer03()
    category = serializers.DictField(source="category_value_and_readable")
    stars = DiscussionStarSerializer01(many=True)
    replies = DiscussionReplySerializer01(many=True)

    class Meta:
        model = Discussion
        fields = ["id", "title", "body", "category", "profile", "stars", "replies", "created_at"]


class DiscussionSerializer02(serializers.ModelSerializer):
    project_id = serializers.IntegerField(source="project.id")

    class Meta:
        model = Discussion
        fields = ["id", "title", "project_id"]


class DiscussionStarSerializer02(serializers.ModelSerializer):
    profile = ProfileSerializer04()
    discussion = DiscussionSerializer02()

    class Meta:
        model = DiscussionStar
        fields = ["id", "profile", "discussion", "created_at"]


class DiscussionReplySerializer02(serializers.ModelSerializer):
    profile = ProfileSerializer03()
    discussion = DiscussionSerializer02()

    class Meta:
        model = DiscussionReply
        fields = ["id", "profile", "discussion", "content", "created_at"]
