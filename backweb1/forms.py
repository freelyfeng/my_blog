from django import forms
from django.contrib.auth.hashers import check_password

from backweb1.models import User


class RegisterForm(forms.Form):

    username = forms.CharField(max_length=20,
                               min_length=5,
                               required=True,
                               error_messages={
                                  'required':'用户名必填',
                                   'max_length':'用户名不能超过20字符',
                                   'min_length':'用户名不能短于5字符',
                                })
    userpwd = forms.CharField(required=True,
                              min_length=8,
                              max_length=20,
                              error_messages={
                                  'required':'用户名必填',
                                  'max_length':'密码不能超过20字符',
                                  'min_length':'密码不能短于8字符',

                              })

    againpwd = forms.CharField(required=True,
                              min_length=8,
                              max_length=20,
                              error_messages={
                                  'required':'用户名必填',
                                  'max_length':'密码不能超过20字符',
                                  'min_length':'密码不能短于8字符',

                              })

    def clean_username(self):
        # 校检注册的账号是否存在
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).first()
        if user:
            print('该账号已存在')
            raise forms.ValidationError('该账号已存在，请更换账号再注册')
        return self.cleaned_data['username']

    def clean(self):
        # 校检密码是否一致
        userpwd = self.cleaned_data.get('userpwd')
        againpwd = self.cleaned_data.get('againpwd')
        if userpwd != againpwd:
            raise forms.ValidationError({'againpwd':'两次密码不一致'})
        return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20,
                               min_length=5,
                               required=True,
                               error_messages={
                                   'required':'用户名必填',
                                   'max_length':'用户名不能超过20字符',
                                   'min_length':'用户名不能短于5字符'
                               })

    userpwd = forms.CharField(required=True,
                              min_length=8,
                              max_length=20,
                              error_messages={
                                  'required':'密码必须填',
                                  'max_length':'密码不能超过20字符',
                                  'min_length':'密码不能短于8字符'
                              })

    def clean(self):
        # 校检用户名是否已注册
        username = self.cleaned_data.get('username')
        user = User.objects.filter(username=username).first()
        if not user:
            raise forms.ValidationError({'username':'该账号没有注册，请去注册'})
        #校检密码

        userpwd = self.cleaned_data.get('userpwd')
        if not check_password(userpwd,user.password):
            raise forms.ValidationError({'pwd':'密码错误'})
        return self.cleaned_data