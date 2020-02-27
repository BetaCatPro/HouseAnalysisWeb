"""HouseAnalysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import xadmin
from django.urls import path,re_path, include

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from house.views import HouseListViewSet


router = DefaultRouter()
router.register(r'v1/api/all_house', HouseListViewSet, base_name="house")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    re_path(r'docs/', include_docs_urls(title="HA")),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]
