from rest_framework import serializers
from .models import Moviedata

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        image = serializers.ImageField(max_length=None, use_url=True)
        model = Moviedata
        fields = ['id', 'name', 'duration', 'rating', 'movie_type', 'image']