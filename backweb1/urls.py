from  django.urls import path
from blog.settings import MEDIA_URL,MEDIA_ROOT


from backweb1 import views

urlpatterns = [

    # 注册账号：
    path('register/',views.register,name='register'),

    # 登录功能
    path('login/',views.login,name='login'),

    # 退出登录
    path('logout/',views.login,name='logout'),

    # 文章功能
    path('article/',views.article,name='article'),

    # 添加文章
    path('add_article/',views.add_article,name='add_article'),

    # 修改文章
    path('update_article/<int:id>/',views.update_article,name='update_article'),

    # 删除文章
    path('del_article/<int:id>/',views.del_article,name='del_article'),

    # 增加栏目
    path('category/',views.category,name='category'),

    # 修改栏目
    path('update_category/<int:id>/',views.update_category,name='update_category'),

    # 删除栏目
    path('del_category/<int:id>/',views.del_category,name='del_category'),
]


from django.contrib.staticfiles.urls import static
urlpatterns += static(MEDIA_URL,document_root=MEDIA_ROOT)