from django.shortcuts import render

# 首页
def index(request):
    if request.method == 'GET':

        return render(request,'web/index.html')

# 关于我
def about(request):
    if request.method == 'GET':

        return render(request,'web/about.html')

# 留言
def gbook(request):

    if request.method == 'GET':

        return render(request,'web/gbook.html')

# 第一个内容页
def info(request):
    if request.method == 'GET':
        return render(request, 'web/info.html')

# 第二个内容页
def infopic(request):
    if request.method == 'GET':
        return render(request, 'web/infopic.html')

# 日记
def list(request):
    if request.method == 'GET':
        return render(request, 'web/list.html')

# 我的照片
def share(request):
    if request.method == 'GET':
        return render(request, 'web/share.html')