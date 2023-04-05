from rest_framework.serializers import ModelSerializer

from fitness_site.models import Video


class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'