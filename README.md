# HouseAnalysisWeb
基于joint-spider爬虫数据的Web端数据可视化平台，[在线访问][1]

数据源来自项目 [Joint-spider][2] 

后端: django-restframework

前端: Vue

[1]: http://120.25.197.182
[2]: https://github.com/BetaCatPro/Joint-spiders

### 应用技术

- Python 后端
  - django-restframework
  - redis
  - mysql
- Web 前端
  - Vue 全家桶
  - echarts
  - element-ui
- 百度地图
  - Web服务API
  - vue-baidu-map

### 环境配置及项目启动

```shell
# 环境配置需要 python3.7 redis mysql vue vue-cli3.x
# 
# 项目启动
# 1. 后端服务启动,进入项目\HouseAnalysis\
 	 python manage.py runserver
# 2. 前端项目启动,进入项目目录\HouseAnalysisWeb\
	 npm run dev
# 3. 前端项目打包
	 npm run build-prod
# 4. 访问地址:http://localhost:9527/
# 5. 后端接口地址: http://localhost:8000/
```

#### 项目持续改进中......

### 注意事项

- mysql及redis服务配置均在\HouseAnalysis\HouseAnalysis\settings.py文件中进行配置
- utils文件夹下文件功能:
  - 插入数据分析结果信息至MySQL:Insert.py
  - 插入基本总信息至Redis:insertRedis.py
  - 插入区划及小区信息至MySQL:com_pro.py

##### 前端页面展示

1. 房源信息页面

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200426160702363.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2J5NjY3MTcxNQ==,size_16,color_FFFFFF,t_70)


2. 房价分析-数据探索分析可视化页面

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200426160715834.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2J5NjY3MTcxNQ==,size_16,color_FFFFFF,t_70)


3. 房价分析-各区划详细信息页面

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200426160738530.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2J5NjY3MTcxNQ==,size_16,color_FFFFFF,t_70)


4. 区划小区详情

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200426160921147.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2J5NjY3MTcxNQ==,size_16,color_FFFFFF,t_70)


5. 小区房源列表详情
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200426160910311.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2J5NjY3MTcxNQ==,size_16,color_FFFFFF,t_70)


6. 搜索房源页面
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200426160855963.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2J5NjY3MTcxNQ==,size_16,color_FFFFFF,t_70)


7. 具体房源详情页面
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200426160843567.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2J5NjY3MTcxNQ==,size_16,color_FFFFFF,t_70)



8. 房屋周边

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200426160814163.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2J5NjY3MTcxNQ==,size_16,color_FFFFFF,t_70)

9. 房源热力信息图页面

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200426160727195.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2J5NjY3MTcxNQ==,size_16,color_FFFFFF,t_70)
## 项目介绍:

### 一. 系统功能架构

1. **后端**

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200426162910669.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2J5NjY3MTcxNQ==,size_16,color_FFFFFF,t_70#pic_center)


2. **前端**、

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200426162921805.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2J5NjY3MTcxNQ==,size_16,color_FFFFFF,t_70#pic_center)


### 二. 系统实现

#### 1) 后端部分

```shell
# 项目依赖
Django==2.1.5
django-cors-headers==2.4.0
django-crispy-forms==1.7.2
django-filter==2.0.0
django-formtools==2.1
django-guardian==1.4.9
django-import-export==1.1.0
django-redis==4.10.0
django-reversion==3.0.2
djangorestframework==3.9.0
djangorestframework-jwt==1.11.0
drf-extensions==0.4.0
PyMySQL==0.9.3
redis==3.0.1
SQLAlchemy==1.3.2
```

**基本流程**

- Django生命周期:

  前端发送请求-->Django的wsgi-->中间件-->路由系统-->视图-->ORM数据库操作-->模板-->返回数据给用户

- rest framework生命周期：

  前端发送请求-->Django的wsgi-->中间件-->路由系统_执行CBV的as_view()，就是执行内部的dispath方法-->在执行dispath之前，有版本分析 和 渲染器-->在dispath内，对request封装-->版本-->认证-->权限-->限流-->视图-->如果视图用到缓存( request.data or  request.query_params )就用到了 解析器-->视图处理数据，用到了序列化(对数据进行序列化或验证) -->视图返回数据可以用到分页

1. 基本接口框架搭建

```shell
# 1. 初始化项目
django-admin startproject HouseAnalysis
# 2. 创建相关应用
cd HouseAnalysis
django-admin startapp house
```

2. 配置xadmin后台可视化管理系统

```shell
# 项目根目录下创建extra_app 文件夹，存放xadmin压缩文件，运行
pip3 install xadmin
```

3. 配置基本项目信息

```shell
# 1. 配置settings.py 文件 位于\\HouseAnalysis\HouseAnalysis\settings.py
# 找到INSTALLED_APPS,加入配置项
	'corsheaders',
 	'xadmin',
    'crispy_forms',
    'rest_framework',
    'django_filters',
    'house'
# 上述配置向是用于将app注册到项目中
# 2. 增加跨域支持
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    '*'
)
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)
CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)
# 3. 在DATABASES中配置MySQL数据库信息
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'house',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS':{
            'init_command':"SET sql_mode='STRICT_TRANS_TABLES'"
        },
    }
}
# 4. 配置drf缓存
REST_FRAMEWORK_EXTENSIONS = {
    #10s后失效
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 10
}
# 5. 配置redis缓存
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/3",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
```

*注：本项目为接口开发不涉及template模板及static静态资源，所以不用对这两项进行配置*

2. 配置接口文档

进入\\HouseAnalysis\HouseAnalysis\urls.py，配置路由信息：

添加`path('xadmin/', xadmin.site.urls)`,
    `re_path(r'docs/', include_docs_urls(title="HA"))`,到`urlpatterns`列表,xadmin为管理页面路由，

docs为接口文档路由，通过http://localhost:8000/docs/可进行访问，如下图：


![](imgs/接口文档.png)

3. 数据model设计

Django Model设计是Django五项基础核心设计之一（Model设计，URL配置，View编写，Template设计，From使用），也是MVC(MVT)模式中重要的环节。

Model是数据模型，并不是数据库，它描述了数据的构成和他们之间的逻辑关系，在Django中，Model设计实质上就是一个类。每一个模型都映射一张数据库表。

- 每个模型都是一个 Python 的类，这些类继承 django.db.models.Model；
- 模型类的每个属性都相当于一个数据库的字段；
- 利用这些，Django 提供了一个自动生成访问数据库的 API；

进入\HouseAnalysis\house\models.py ,添加`Api，Elevator，Floor，Layout，Region，Decortion，Purposes，Orientation，Constructure，Community，CommunityRange`模型,用以提供数据进行序列化。

model创建完成后进行数据迁移：

```shell
# 进入项目根目录
python manage.py makemigrations
# 同步至数据库
python manage.py migrate
```

4. 序列化器设计

在house文件夹下新建文件serializer.py 文件，用来进行数据序列化。

定义序列化器（本质就是一个类），一般包括模型类的字段，有自己的字段类型规则。实现了序列化器后，就可以创建序列化对象以及查询集进行序列化操作，通过序列化对象.data来获取数据（不用自己构造字典，再返回Json数据）

- 用于序列化时，将模型类对象传入**instance**参数

- 用于反序列化时，将要被反序列化的数据传入**data**参数

- 除了instance和data参数外，在构造Serializer对象时，还可通过**context**参数额外添加数据

这里我们使用模型序列化器(ModelSerializer)，ModelSerializer与常规的Serializer相同，但提供了：

- 基于模型类自动生成一系列字段
- 基于模型类自动为Serializer生成validators，比如unique_together
- 包含默认的create()和update()的实现

例如：利用简单代码就可序列化house内容

```python
class HouseSerializer(serializers.ModelSerializer):

    class Meta:
        # 需要序列化的model
        model = Api
        # 需要序列化的字段
        fields = "__all__"
```

同理，将剩余的model序列化，包括`ElevatorSerializer，FloorSerializer，LayoutSerializer，RegionSerializer，RegionS，CommunitySerializer，CommunityRangeSerializer，DecortionSerializer，PurposesSerializer，ConstructureSerializer，OrientationSerializer`，其中，`RegionS`序列化器作为`CommunitySerializer`和`CommunityRangeSerializer`的上级序列化器。

5. 视图View：

视图的功能：说白了就是接收前端请求，进行数据处理

（这里的处理包括：如果前端是GET请求，则构造查询集，将结果返回，这个过程为**序列化**；如果前端是POST请求，假如要对数据库进行改动，则需要拿到前端发来的数据，进行校验，将数据写入数据库，这个过程称为**反序列化**）

最原始的视图可以实现这样的逻辑处理，但是针对不同的请求，需要在类视图中定义多个方法实现各自的处理，这样是可以解决问题，但是存在一个缺陷，那就是每个函数中一般的逻辑都差不多：读请求，从数据库拿数据，写东西到数据库，返回结果给前端。这样就会产生大量的重复代码。

在开发REST API的视图中，虽然每个视图具体操作的数据不同，但增、删、改、查的实现流程基本套路化，所以这部分代码也是可以复用简化编写的：

**增**：校验请求数据 -> 执行反序列化过程 -> 保存数据库 -> 将保存的对象序列化并返回

**删**：判断要删除的数据是否存在 -> 执行数据库删除

**改**：判断要修改的数据是否存在 -> 校验请求的数据 -> 执行反序列化过程 -> 保存数据库 -> 将保存的对象序列化并返回

**查**：查询数据库 -> 将数据序列化并返回

视图编写在views.py 文件中，这里我们使用类识图的方式进行开发。

- 对于GET请求，我们需要返回一个列表，例如对于请求为：`http://127.0.0.1/api/v1/allhouse`，我们需要将所有房源信息的序列化结果返回暴露出去。
- 对于GET/:ID请求，我们需要返回一个对用结果，例如对于请求为：`http://127.0.0.1/api/v1/allhouse`/1，我们需要将房源id(此时的id可配置为指定需求参数)为1的序列化结果返回暴露出去。
- 对于POST请求，我们需要新建一条信息，例如对于post请求参数为：`{id:xxx,values:xxx...}`，我们需要当前信息做检验，合法后将当前数据添加到数据库中。
- 对于PATCH请求：更新某个指定房源的信息。
- 对于DELETE请求：删除某个房源信息。

例：

```python
# CacheResponseMixin: 缓存，内存级别
# ListModelMixin处理GET（all）请求
# RetrieveModelMixin处理（id）请求
# 基础类GenericViewSet，提供分页，过滤，排序等功能
class HouseListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Api.objects.all()
    # 房源序列化
    serializer_class = HouseSerializer
    # 房源分页
    pagination_class = HousePagination
    # 自定义排序，过滤类
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # 过滤信息字段
    filter_fields = ('price',)
    # 搜搜字段
    search_fields = ('title', 'region', 'community_name')
    # 排序字段
    ordering_fields = ('price', 'unit_price','construction_area')
	
    # 重写retrieve方法，实现获取单个序列化对象信息
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

# 分页配置项
class HousePagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100
```

其他视图类似，包括：`ElevaorViewSet，FloorViewSet，LayoutViewSet，RegionViewSet，CommunityViewSet，CommunityPagination，AllCommunityViewSet，CommunityRangeViewSet，DecortionViewSet，PurposesViewSet，ConstructureViewSet，OrientationViewSet`

其中对于`CommunityViewSet`类，我们需要根据具体的community_id来返回其所有信息，这时就不能用`RetrieveModelMixin`类的`retrieve`方法了，需要重写`get_queryset`方法，返回特定的model。

```python
    def get_queryset(self):
        if self.request.GET['rid'] == '0' :
            # 获取所有
            return  Community.objects.all()
        else:
            return Community.objects.filter(region=self.request.GET['rid'])
```

*其他参数*

- ?limit=10：指定返回记录的数量
- ?offset=10：指定返回记录的开始位置。
- ?page=2&per_page=100：指定第几页，以及每页的记录数。
- ?sort=name&order=asc：指定返回结果按照哪个属性排序，以及排序顺序。
- ?animal_type_id=1：指定筛选条件



6. 路由配置

使用`rest_framework`的`DefaultRouter`进行路由注册：

```python
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'v1/api/all_house', HouseListViewSet, base_name="house")
......
```

将router加入到urlpatterns中：

```python
path('', include(router.urls)),
```

这时当有请求访问到存在的路由后，路由会将请求转发到视图类，在视图类中将请求处理后，返回序列化结果，即后端暴露的接口数据。

7. 关于接口数据

![](imgs/接口数据.png)

**数据描述**

- count : 总数据量
- next： 下一页url
- previous： 上一页url
- results: 结果集

HTTP状态码：

- 200 OK - [GET]：服务器成功返回用户请求的数据，该操作是幂等的（Idempotent）。
- 201 CREATED - [POST/PUT/PATCH]：用户新建或修改数据成功。
- 202 Accepted - [*]：表示一个请求已经进入后台排队（异步任务）
- 204 NO CONTENT - [DELETE]：用户删除数据成功。
- 400 INVALID REQUEST - [POST/PUT/PATCH]：用户发出的请求有错误，服务器没有进行新建或修改数据的操作，该操作是幂等的。
- 401 Unauthorized - [*]：表示用户没有权限（令牌、用户名、密码错误）。
- 403 Forbidden - [*] 表示用户得到授权（与401错误相对），但是访问是被禁止的。
- 404 NOT FOUND - [*]：用户发出的请求针对的是不存在的记录，服务器没有进行操作，该操作是幂等的。
- 406 Not Acceptable - [GET]：用户请求的格式不可得（比如用户请求JSON格式，但是只有XML格式）。
- 410 Gone -[GET]：用户请求的资源被永久删除，且不会再得到的。
- 422 Unprocesable entity - [POST/PUT/PATCH] 当创建一个对象时，发生一个验证错误。
- 500 INTERNAL SERVER ERROR - [*]：服务器发生错误，用户将无法判断发出的请求是否成功。

8. 关于具体数据处理-为了更方便序列化

- 将总体信息数据存放到Redis数据库中，减少后端处理请求是进行大量数据操作是运算量

```python
# 将所有房源数，小区数，总体单价价均价，总体总价均价，存入redis
def insertIndexInfo():
    all_number = house.count()
    com_number = Api.objects.values('community_name').distinct().count()
    mean_price = format(house.aggregate(Avg('price'))['price__avg'],'.3f')
    mean_unit_price = format(house.aggregate(Avg('unit_price'))['unit_price__avg'],'.3f')
    data = {
        "all_number": all_number,
        "com_number": com_number,
        "mean_price": mean_price,
        "mean_unit_price": mean_unit_price
    }

    redis_conn.mset(data)
```

- 将处理好的数据存入MySQL，包括(电梯，装修情况等信息)

```python
# 1. 定义专门数据库操作类InsertIntoMysql
class InsertIntoMysql():

    # 属性中定义sql语句获取数据
    def __init__(self):
        self.elevator_sql = 'select unit_price, price, elevator from house_api'
        # ......
	
    # 定义数据插入方法
    def insertElevator(self):
        index, values, price_mean, unit_price_mean = multiple(self.elevator_sql, engine, 'elevator')
        for i in range(len(index)):
            elevator = Elevator()
            elevator.version = 'v1'
            elevator.title = '电梯分布情况'
            elevator.has_ele = index[i]
            elevator.el_num = values[i]
            elevator.mean_price = price_mean[i]
            elevator.mean_unit_price = unit_price_mean[i]
            elevator.save()
     # 其他剩余数据插入方法
     # ......
# 2. 数据处理模块，包括单因子和对因子处理
#	 利用数据处理模块pandas
def single(sql,engine,feature):
    """
    :param sql: sql语句
    :param engine: mysql引擎
    :param feature: 数据特征
    :return: 特征，数量
    """
    df_sql = sql
    df = pd.read_sql(df_sql, engine)
    df[feature] = df[feature].astype(str)
    if feature=='floor':
        df[df[feature]=='暂无数据'] = '18'
        df[feature] = df[feature].apply(lambda x: re.findall('\d+',x)[0])
    feature_res = df[feature].value_counts()
    index = feature_res.index
    values = feature_res.values
    return index,values

def multiple(sql,engine,feature):
    """
    :param sql: sql语句
    :param engine: mysql引擎
    :param feature: 数据特征
    :return: 特征，数量，总价均价，单价均价
    """
    df_sql = sql
    df = pd.read_sql(df_sql, engine)
    df[feature] = df[feature].astype(str)
    if feature == 'region':
        df[feature] = df[feature].apply(lambda x:re.sub(r"\[|\]|'",'',x).split(',')[0])
    feature_res = df[feature].value_counts()
    index = feature_res.index
    values = feature_res.values
    price_mean = []
    unit_price_mean = []
    max_unit_price = []
    min_unit_price = []
    for inx,val in zip(index,values):
        price_mean.append(format(df[df[feature]==inx]['price'].astype(float).mean(),'.3f'))
        unit_price_mean.append(format(df[df[feature]==inx]['unit_price'].astype(float).mean(),'.3f'))
        max_unit_price.append(format(df[df[feature]==inx]['unit_price'].astype(float).max(),'.3f'))
        min_unit_price.append(format(df[df[feature]==inx]['unit_price'].astype(float).min(),'.3f'))
    return index, values, price_mean, unit_price_mean, max_unit_price, min_unit_price
```

#### 2) 前端部分

