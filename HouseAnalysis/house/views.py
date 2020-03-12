import json
from django.shortcuts import HttpResponse
from django.views.generic.base import View
from django.db.models import Avg

from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

#缓存（内存级别）
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .models import Api
from .serializers import HouseSerializer, ElevatorSerializer

# Create your views here.


class HousePagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class HouseListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Api.objects.all()
    serializer_class = HouseSerializer
    pagination_class = HousePagination
    search_fields = ('title', 'region', 'community_name')
    ordering_fields = ('price', 'unit_price')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ElevaorViewSet(CacheResponseMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Api.objects.all()
    serializer_class = ElevatorSerializer
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class Elevator(View):
    def get(self, request):
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
        return HttpResponse(res_json, content_type='application/json')
