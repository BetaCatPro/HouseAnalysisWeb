from rest_framework import serializers

from house.models import Api


class HouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Api
        fields = "__all__"