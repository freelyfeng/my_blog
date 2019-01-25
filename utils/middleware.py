import re

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from backweb1.models import User


class AuthMiddleware(MiddlewareMixin):

    def process_request(self,request):
        # 拦截请求之前的函数
        # 1.给request.user属性赋值，赋值为当前登录系统的用户
        # 拿到当前登录用户的id
        user_id = request.session.get('user_id')
        if user_id:
            # 拿到当前登录页面的用户的对象
            user = User.objects.filter(pk=user_id).first()
            # 把对象赋值为当前登录的对象
            request.user = user

        path = request.path
        if path == '/':
            return None
        # 不需要做校验的路由
        not_need_check = ['/backweb1/login/','/backweb1/register/','/webevent/.*/']
        for check_path in not_need_check:
            if re.match(check_path, path):
                # 当前path路径为不需要做登录校验的路由
                return None

        if not user_id:
            return HttpResponseRedirect(reverse('backweb1:login'))