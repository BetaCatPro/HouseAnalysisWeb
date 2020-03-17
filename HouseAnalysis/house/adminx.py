import xadmin
from xadmin import views
from .models import Api, Elevator, Floor, Layout, Region, Decortion, Purposes, Orientation, Constructure


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "数据后台"
    site_footer = "HA"
    # menu_style = "accordion"

"""
    title,price,unit_price,community_name,
    region,type,construction_area,
    orientation,decoration,floor,
    elevator,purposes,release_date,
    house_structure,image_urls,from_url
"""

class ApiAdmin(object):
    list_display = ['title', 'price', "unit_price",
                    'community_name', 'region', 'type','construction_area',
                    'orientation', 'decoration', "floor",
                    'elevator', 'purposes','house_structure', 'image_urls', "from_url"]

class ElevatorAdmin(object):
    list_display = ['version','title','has_ele','el_num','mean_price','mean_unit_price']

class FloorAdmin(object):
    list_display = ['version','title','floor','num']

class LayoutAdmin(object):
    list_display = ['version','title','layout','num']

class RegionAdmin(object):
    list_display = ['version','title','region','num','mean_price','mean_unit_price']

class DecorationAdmin(object):
    list_display = ['version','title','decoration','num','mean_price','mean_unit_price']

class PurposesAdmin(object):
    list_display = ['version','title','purposes','num']

class OrientationAdmin(object):
    list_display = ['version','title','orientation','num']

class ConstructureAdmin(object):
    list_display = ['version','title','constructure','num']

xadmin.site.register(Api, ApiAdmin)
xadmin.site.register(Elevator, ElevatorAdmin)
xadmin.site.register(Floor, FloorAdmin)
xadmin.site.register(Layout, LayoutAdmin)
xadmin.site.register(Region, RegionAdmin)
xadmin.site.register(Decortion, DecorationAdmin)
xadmin.site.register(Purposes, PurposesAdmin)
xadmin.site.register(Orientation, OrientationAdmin)
xadmin.site.register(Constructure, ConstructureAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)