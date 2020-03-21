import json
from django.shortcuts import HttpResponse
from django.views.generic.base import View
from django.db.models import Avg

from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

# 缓存（内存级别）
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .models import Api, Elevator, Floor, Layout, Region, Decortion, Purposes, Orientation, Constructure, Community,CommunityRange
from .serializers import HouseSerializer, ElevatorSerializer, FloorSerializer, LayoutSerializer
from .serializers import RegionSerializer, DecortionSerializer, PurposesSerializer, OrientationSerializer, ConstructureSerializer
from .serializers import CommunitySerializer,CommunityRangeSerializer

from utils.getinfo import res

# Create your views here.


class HousePagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

class index(View):
    def get(self,request):
        data = res
        res_json = json.dumps(data)
        return HttpResponse(res_json, content_type='application/json')

class HouseListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Api.objects.all()
    serializer_class = HouseSerializer
    pagination_class = HousePagination
    search_fields = ('title', 'region', 'community_name')
    ordering_fields = ('price', 'unit_price')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ElevaorViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class FloorViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class LayoutViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Layout.objects.all()
    serializer_class = LayoutSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class RegionViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class CommunityViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,GenericViewSet):
    pagination_class = HousePagination
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class CommunityRangeViewSet(CacheResponseMixin, mixins.ListModelMixin,GenericViewSet):
    pagination_class = HousePagination
    queryset = CommunityRange.objects.all()
    serializer_class = CommunityRangeSerializer

class DecortionViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Decortion.objects.all()
    serializer_class = DecortionSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class PurposesViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Purposes.objects.all()
    serializer_class = PurposesSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ConstructureViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Constructure.objects.all()
    serializer_class = ConstructureSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class OrientationViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Orientation.objects.all()
    serializer_class = OrientationSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

