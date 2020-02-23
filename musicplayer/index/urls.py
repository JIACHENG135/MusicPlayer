from django.urls import path,re_path
from . import views
from django.views.generic import TemplateView
# 设置首页的URL地址信息
urlpatterns = [
    
    re_path(r"^addAlbum/",views.carouselAPI),
    path('searchSong/<str:keyword>',views.indexView),
    path('updateList/<str:albumID>',views.getAlbumInfo),

]