from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest
from django.http import HttpResponse
# 定义视图函数
def index(request):
    context = {
        'name':'想了解更多吗?点击我哦'
    }
     # 请求
    # 参数2: 模板文件
    return render(request,'book/index.html',context=context)
