from rest_framework import serializers
from games.models import TEST


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = TEST
        fields = ('id', 'title', 'tutorial_url', 'image_path', 'description',
                  'published')
