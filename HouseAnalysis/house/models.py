from django.db import models
from utils.base_model import BaseModel

# Create your models here.
class Api(BaseModel):
    """
    title,price,unit_price,community_name,
    region,type,construction_area,
    orientation,decoration,floor,
    elevator,purposes,release_date,
    house_structure,image_urls,from_url
    """
    title = models.CharField(max_length=500, verbose_name="名称")
    price = models.CharField(max_length=50, default="", verbose_name="总价")
    unit_price = models.CharField(max_length=50, verbose_name="单价")
    community_name = models.CharField(max_length=100, verbose_name="小区名")
    region = models.CharField(max_length=50, verbose_name="区域")
    type = models.CharField(max_length=50, verbose_name="户型")
    construction_area = models.CharField(max_length=20, verbose_name="建筑面积")
    orientation = models.CharField(max_length=10, verbose_name="朝向")
    decoration = models.CharField(max_length=10, verbose_name="装修情况")
    floor = models.CharField(max_length=15, verbose_name="楼层")
    elevator = models.CharField(max_length=10, verbose_name="电梯")
    purposes = models.CharField(max_length=15, verbose_name="房屋类型")
    release_date = models.DateTimeField(verbose_name="挂牌时间")
    house_structure = models.CharField(max_length=20, verbose_name="建筑类型")
    image_urls = models.CharField(max_length=1500, verbose_name="房屋详情图")
    from_url = models.CharField(max_length=100, verbose_name="房屋链接")

    class Meta:
        verbose_name = 'house_info'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title