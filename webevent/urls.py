
from  django.urls import path

from webevent import views

urlpatterns = [
    # 网站首页路由
    path('index/',views.index,name='index'),
    # 关于我路由
    path('about/',views.about,name='about'),
    # 留言路由
    path('gbook/',views.gbook,name='gbook'),
    # 第一个内容页路由
    path('info/',views.info,name='info'),
    # 第二个内容页路由
    path('infopic/',views.infopic,name='infopic'),
    # 我的日记路由
    path('list/',views.list,name='list'),
    # 我的相册路由
    path('share/',views.share,name='share'),
]