from rest_framework import serializers
from django.db.models import Avg

import json
from house.models import Api

class HouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Api
        fields = "__all__"

class ElevatorSerializer(serializers.ModelSerializer):
    result = serializers.SerializerMethodField()

    def get_result(self,obj):
        h = Api.objects.filter(elevator='有')
        n = Api.objects.filter(elevator='无')
        has_el_num = h.count()
        has_mean_price = h.aggregate(Avg('price'))
        has_mean_unit_price = h.aggregate(Avg('unit_price'))
        no_el_num = n.count()
        no_mean_price = n.aggregate(Avg('price'))
        no_mean_unit_price = n.aggregate(Avg('unit_price'))

        data = {
            "has_el_num":has_el_num,
            "no_el_num":no_el_num,
            "has_mean_price":has_mean_price,
            "has_mean_unit_price":has_mean_unit_price,
            "no_mean_price":no_mean_price,
            "no_mean_unit_price":no_mean_unit_price
        }
        res_json = json.dumps(data,sort_keys=True)

        return res_json

    class Meta:
        model = Api
        fields = ('result',)