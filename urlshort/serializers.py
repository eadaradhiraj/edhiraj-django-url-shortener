from rest_framework import serializers
from . import models


class UrlSerializer(serializers.ModelSerializer):
    # Serializer for the url model, in fields we specify the model attributes we want to
    # deserialize and serialize
    # slug = serializers.PrimaryKeyRelatedField(queryset=models.UrlData.objects.all())
    class Meta:
        model = models.UrlData
        fields = ['url', 'slug']
