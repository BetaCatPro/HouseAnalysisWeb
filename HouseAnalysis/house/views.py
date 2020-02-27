from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

#缓存（内存级别）
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .models import Api
from .serializers import HouseSerializer

# Create your views here.


class HousePagination(PageNumberPagination):
    page_size = 12
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
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


from django.views.generic.base import View

from house.models import Api


class MeanPriceView(View):
    """
    各个小区房屋均价
    """

    def get(self, request):
        import json
        json_list = []
        goods = Api.object.all()[:10]
        # 1.0原始方法
        # for good in goods:
        #     json_dict = {}
        #     json_dict['name'] = good.name
        #     json_dict['category'] = good.category
        #     json_dict['market_price'] = good.market_price
        #     json_list.append(json_dict)

        # 2.0model_to_dict方法
        # from django.forms.models import model_to_dict
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)

        # 3.0序列化, （上面的方法都不能序列化datetime，image等）
        from django.core import serializers
        json_data = serializers('json', goods)
        json_data = json.loads(json_data)
        from django.http import HttpResponse, JsonResponse
        # return HttpResponse(json.dumps(json_list), content_type='application/json')
        return JsonResponse(json_data, safe=False)

