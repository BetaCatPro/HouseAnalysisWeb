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
