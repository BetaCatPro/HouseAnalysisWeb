import json
from django.shortcuts import HttpResponse
from django.views.generic.base import View
from django.db.models import Avg

from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

# 缓存（内存级别）
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .models import Api, Elevator, Floor, Layout, Region, Decortion, Purposes, Orientation, Constructure, Community,CommunityRange
from .serializers import HouseSerializer, ElevatorSerializer, FloorSerializer, LayoutSerializer
from .serializers import RegionSerializer, DecortionSerializer, PurposesSerializer, OrientationSerializer, ConstructureSerializer
from .serializers import CommunitySerializer,CommunityRangeSerializer,PositionSerializer

from utils.getinfo import res

class HousePagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

class PositionPagination(PageNumberPagination):
    page_size = 9000
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
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('price',)
    search_fields = ('title', 'region', 'community_name')
    ordering_fields = ('price', 'unit_price','construction_area')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class PositionViewSet(CacheResponseMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Api.objects.all()
    pagination_class = PositionPagination
    serializer_class = PositionSerializer

class ElevaorViewSet(CacheResponseMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer


class FloorViewSet(CacheResponseMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer


class LayoutViewSet(CacheResponseMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Layout.objects.all()
    serializer_class = LayoutSerializer


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
    # lookup_field = 'region'


    # def get_object(self):
    #     queryset = Community.objects.filter(region__id=self.request.rid)
    #
    #     return queryset

    def get_queryset(self):
        if self.request.GET['rid'] == '0' :
            # 获取所有
            return  Community.objects.all()
        else:
            return Community.objects.filter(region=self.request.GET['rid'])

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class CommunityPagination(PageNumberPagination):
    page_size = 2000
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

class AllCommunityViewSet(CacheResponseMixin, mixins.ListModelMixin,GenericViewSet):
    # 不采取分页
    # pagination_class = CommunityPagination
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

    def get_queryset(self):
        return  Community.objects.filter(rangeIndex=self.request.GET['rangeindex'])

class CommunityRangeViewSet(CacheResponseMixin, mixins.ListModelMixin,GenericViewSet):
    pagination_class = HousePagination
    queryset = CommunityRange.objects.all()
    serializer_class = CommunityRangeSerializer

    def get_queryset(self):
        return CommunityRange.objects.filter(region=self.request.GET['rid'])

class DecortionViewSet(CacheResponseMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Decortion.objects.all()
    serializer_class = DecortionSerializer


class PurposesViewSet(CacheResponseMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Purposes.objects.all()
    serializer_class = PurposesSerializer


class ConstructureViewSet(CacheResponseMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Constructure.objects.all()
    serializer_class = ConstructureSerializer


class OrientationViewSet(CacheResponseMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Orientation.objects.all()
    serializer_class = OrientationSerializer

