import xadmin
from xadmin import views
from .models import Api


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


xadmin.site.register(Api, ApiAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)