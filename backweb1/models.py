from django.db import models

class User(models.Model):
    """
    登录表
    """
    username = models.CharField(max_length=20,unique=True,verbose_name='用户名')
    password = models.CharField(max_length=255,unique=True,verbose_name='用户密码')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间',null=True)

    class Meta:
        db_table = 'user'

class Colu(models.Model):
    """
    栏目
    """
    c_name = models.CharField(max_length=20,unique=True,verbose_name='栏目的名字')
    c_alias = models.CharField(max_length=20,unique=True,verbose_name='栏目的别名')
    c_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

    class Meta:
        db_table = 'colu'




class Article(models.Model):
    """
    文章表
    """
    a_title = models.CharField(max_length=50,unique=True,verbose_name='文章标题')
    a_content = models.TextField(null=True)
    a_column = models.ForeignKey(Colu,verbose_name='文章栏目',on_delete=models.CASCADE)
    a_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    a_image = models.ImageField(upload_to='upload',null=True)

    class Meta:
        db_table = 'article'


