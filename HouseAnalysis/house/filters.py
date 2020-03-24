import django_filters
from django.db.models import Q

from .models import Api


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """
    #不用写name='shop_price'
    pricemin = django_filters.NumberFilter('price', help_text="最低价格", lookup_expr='gte')
    pricemax = django_filters.NumberFilter('price', help_text="最低价格", lookup_expr='lte')

    class Meta:
        model = Api
        fields = ['pricemin', 'pricemax']
