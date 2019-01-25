from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# from backweb1.forms import LoginForm
from backweb1.forms import RegisterForm, LoginForm
from backweb1.models import User, Article, Colu

# 注册页面
def register(request):
    if request.method == 'GET':
        return render(request,'backweb/register.html')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
        # 账号不存在于数据库中，密码和确认密码一致
            username = form.cleaned_data['username']
            password = make_password(form.cleaned_data['userpwd'])

            # 把账号保存到数据库中
            User.objects.create(username=username,
                                password=password,
                                )
            return HttpResponseRedirect(reverse('backweb1:login'))
        else:
            # 获取表单严重不通过的错误信息
            errors = form.errors

            return render(request, 'backweb/register.html', {'errors': errors})

# 登录页面
def login(request):
    if request.method == 'GET':

        return render(request,'backweb/login.html')

    if request.method == 'POST':
        # username = request.POST.get()
        form = LoginForm(request.POST)
        if form.is_valid():
            # 用户名存在，密码相同
            username = form.cleaned_data['username']
            user = User.objects.filter(username=username).first()
            request.session['user_id'] = user.id
            return HttpResponseRedirect(reverse('backweb1:article'))
        else:
            errors = form.errors
            return render(request,'backweb/login.html',{'errors':errors})

# 后台的顶部的退出功能
def logout(request):
    if request.method == 'GET':

        #删除session值
        del request.session['user_id']
        return HttpResponseRedirect(reverse('backweb1:login'))


# 文章页面
def article(request):

    if request.method == 'GET':

        # 获取分页的角码
        page = int(request.GET.get('page',1))

        # 获取数据中文章的信息
        article_all = Article.objects.all()

        # Paginator把文章进行分页
        pg = Paginator(article_all,2)

        # 分页后的信息
        articles = pg.page(page)

        return render(request,'backweb/article.html', {'articles': articles})







# 添加文章信息
def add_article(request):

    if request.method == 'GET':

        colus =  Colu.objects.all()

        return render(request,'backweb/add-article.html',{'colus':colus})

    if request.method == 'POST':
        # 添加文章保存到数据库中
        title = request.POST.get('title')
        content = request.POST.get('content')
        icon = request.FILES.get('icon')
        Article.objects.create(a_title=title,
                               a_content=content,
                               a_image=icon,
                               a_column_id = 1,
                               )
        return HttpResponseRedirect(reverse('backweb1:article'))


# 修改文章信息
def update_article(request,id):
    if request.method == 'GET':
        # 获取文章对象，返回给页面
        colus = Colu.objects.all()

        return render(request,'backweb/update-article.html',{'colus':colus})

    if request.method == 'POST':
        # 拿到网页中修改的文章内容
        title = request.POST.get('title')
        content = request.POST.get('content')



        # 通过传入的路由的id值修改对象
        arti = Article.objects.filter(id=id).first()
        arti.a_title = title
        arti.a_content = content
        arti.save()

        return HttpResponseRedirect(reverse('backweb1:article'))


# 删除文章
def del_article(request,id):

    if request.method == 'GET':
        # 通过路由的传入的 id值删除文章
        Article.objects.filter(id=id).delete()
        return HttpResponseRedirect(reverse('backweb1:article'))



# 添加栏目信息
def category(request):

    if request.method == 'GET':
        # 拿到数据库中所有的栏目对象
        colus = Colu.objects.all()

        return render(request,'backweb/category.html',{'colus':colus})

    if request.method == 'POST':
        # 拿到网页中输入的信息
        name = request.POST.get('name')
        alias = request.POST.get('alias')

        Colu.objects.create(c_name=name,
                            c_alias=alias)

        return HttpResponseRedirect(reverse('backweb1:category'))


#修改栏目信息
def update_category(request,id):

    if request.method == 'GET':

        return render(request,'backweb/update-category.html')

    if request.method == 'POST':
        # 拿到网页中输入的修改信息
        name = request.POST.get('name')
        alias = request.POST.get('alias')

        # 拿到数据中对应的信息，修改信息
        col = Colu.objects.filter(id=id).first()
        col.c_name = name
        col.c_alias = alias
        col.save()

        return HttpResponseRedirect(reverse('backweb1:category'))




# 删除栏目信息

def del_category(request,id):

    if request.method == 'GET':
        # 通过传入的id值来删除栏目信息
        Colu.objects.filter(id=id).delete()

        return HttpResponseRedirect(reverse('backweb1:category'))





