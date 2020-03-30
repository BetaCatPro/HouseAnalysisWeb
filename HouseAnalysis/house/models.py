from django.db import models
# from utils.base_model import BaseModel

# Create your models here.
class Api(models.Model):
    """
    title,price,unit_price,community_name,
    region,type,construction_area,
    orientation,decoration,floor,
    elevator,purposes,release_date,
    house_structure,image_urls,from_url
    """
    title = models.CharField(max_length=500, verbose_name="名称")
    price = models.DecimalField(max_digits=9,decimal_places=1, verbose_name="总价")
    unit_price = models.DecimalField(max_digits=9,decimal_places=1, verbose_name="单价")
    community_name = models.CharField(max_length=100, verbose_name="小区名")
    region = models.CharField(max_length=50, verbose_name="区域")
    type = models.CharField(max_length=50, verbose_name="户型")
    construction_area = models.CharField(max_length=20, verbose_name="建筑面积")
    orientation = models.CharField(max_length=10, verbose_name="朝向")
    decoration = models.CharField(max_length=10, verbose_name="装修情况")
    floor = models.CharField(max_length=15, verbose_name="楼层")
    elevator = models.CharField(max_length=10, verbose_name="电梯")
    purposes = models.CharField(max_length=15, verbose_name="房屋类型")
    release_date = models.DateField(verbose_name="挂牌时间")
    house_structure = models.CharField(max_length=20, verbose_name="建筑类型")
    image_urls = models.CharField(max_length=1500, verbose_name="房屋详情图")
    from_url = models.CharField(max_length=100, verbose_name="房屋链接")
    idi = models.IntegerField()
    lat = models.DecimalField(max_digits=12,decimal_places=9,verbose_name="纬度")
    lng = models.DecimalField(max_digits=12,decimal_places=9,verbose_name="经度")

    class Meta:
        verbose_name = 'house'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class Elevator(models.Model):
    version = models.CharField(max_length=8,verbose_name="接口版本")
    title = models.CharField(max_length=12,verbose_name="接口info")
    has_ele = models.CharField(max_length=3,verbose_name="是否存在电梯")
    el_num = models.IntegerField(verbose_name="房源数")
    mean_price = models.DecimalField(max_digits=8,decimal_places=3,verbose_name="总价均价")
    mean_unit_price = models.DecimalField(max_digits=8,decimal_places=3,verbose_name="单价均价")

    class Meta:
        verbose_name = 'elevatorinfo'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class Floor(models.Model):
    version = models.CharField(max_length=8,verbose_name="接口版本")
    title = models.CharField(max_length=12,verbose_name="接口info")
    floor = models.CharField(max_length=20,verbose_name="楼层")
    num = models.IntegerField(verbose_name="数量")

    class Meta:
        verbose_name = 'floorinfo'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class Layout(models.Model):
    version = models.CharField(max_length=8,verbose_name="接口版本")
    title = models.CharField(max_length=12,verbose_name="接口info")
    layout = models.CharField(max_length=20,verbose_name="户型")
    num = models.IntegerField(verbose_name="数量")

    class Meta:
        verbose_name = 'layoutinfo'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class Region(models.Model):
    version = models.CharField(max_length=8,verbose_name="接口版本")
    title = models.CharField(max_length=12,verbose_name="接口info")
    region = models.CharField(max_length=10,verbose_name="行政区划")
    num = models.IntegerField(verbose_name="数量")
    mean_price = models.DecimalField(max_digits=8, decimal_places=3, verbose_name="总价均价")
    mean_unit_price = models.DecimalField(max_digits=8, decimal_places=3, verbose_name="单价均价")
    max_unit_price = models.DecimalField(max_digits=8, decimal_places=3, verbose_name="最大单价")
    min_unit_price = models.DecimalField(max_digits=8, decimal_places=3, verbose_name="最小单价")

    class Meta:
        verbose_name = 'regioninfo'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class Decortion(models.Model):
    version = models.CharField(max_length=8,verbose_name="接口版本")
    title = models.CharField(max_length=12,verbose_name="接口info")
    decoration = models.CharField(max_length=10,verbose_name="装修情况")
    num = models.IntegerField(verbose_name="数量")
    mean_price = models.DecimalField(max_digits=8, decimal_places=3, verbose_name="总价均价")
    mean_unit_price = models.DecimalField(max_digits=8, decimal_places=3, verbose_name="单价均价")

    class Meta:
        verbose_name = 'decorationinfo'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class Purposes(models.Model):
    version = models.CharField(max_length=8,verbose_name="接口版本")
    title = models.CharField(max_length=12,verbose_name="接口info")
    purposes = models.CharField(max_length=10,verbose_name="房屋用途")
    num = models.IntegerField(verbose_name="数量")

    class Meta:
        verbose_name = 'purposesinfo'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class Orientation(models.Model):
    version = models.CharField(max_length=8,verbose_name="接口版本")
    title = models.CharField(max_length=12,verbose_name="接口info")
    orientation = models.CharField(max_length=15,verbose_name="房屋朝向")
    num = models.IntegerField(verbose_name="数量")

    class Meta:
        verbose_name = 'orientationinfo'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class Constructure(models.Model):
    version = models.CharField(max_length=8,verbose_name="接口版本")
    title = models.CharField(max_length=12,verbose_name="接口info")
    constructure = models.CharField(max_length=10,verbose_name="建筑类型")
    num = models.IntegerField(verbose_name="数量")

    class Meta:
        verbose_name = 'constructureinfo'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class Community(models.Model):
    version = models.CharField(max_length=8, verbose_name="接口版本")
    title = models.CharField(max_length=12, verbose_name="接口info")
    region = models.ForeignKey(Region, on_delete=None,verbose_name="行政区划")
    name = models.CharField(max_length=30,verbose_name="小区名")
    num = models.IntegerField(verbose_name="数量")
    mean_unit_price = models.DecimalField(max_digits=8, decimal_places=3, verbose_name="单价均价")

    class Meta:
        verbose_name = 'Neighbor'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class CommunityRange(models.Model):
    version = models.CharField(max_length=8, verbose_name="接口版本")
    title = models.CharField(max_length=12, verbose_name="接口info")
    region = models.ForeignKey(Region, on_delete=None, verbose_name="行政区划")
    name = models.CharField(max_length=30,verbose_name="小区名")
    mean_unit_price = models.DecimalField(max_digits=8, decimal_places=3, verbose_name="单价均价")

    class Meta:
        verbose_name = 'CommunityRange'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
