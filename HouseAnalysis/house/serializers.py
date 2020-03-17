from rest_framework import serializers

from house.models import Api,Elevator,Floor,Layout,Region,Decortion,Purposes,Orientation,Constructure

class HouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Api
        fields = "__all__"

class ElevatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Elevator
        fields = "__all__"

class FloorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Floor
        fields = "__all__"


class LayoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Layout
        fields = "__all__"


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"


class DecortionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decortion
        fields = "__all__"

class PurposesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purposes
        fields = "__all__"

class ConstructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Constructure
        fields = "__all__"

class OrientationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orientation
        fields = "__all__"