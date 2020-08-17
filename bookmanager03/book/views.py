from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
# Create your views here.
def index(request):

    return HttpResponse("OK")

from book.models import BookInfo
books = BookInfo.objects.all()
#导入分页类
from django.core.paginator import Paginator
#创建分页实例 表名和个数
p=Paginator(books,2)
# 显示页数
p.num_pages
# 获取第一页的数据
page1 = p.page(1)
# 显示第一页的数据
page1.object_list
# 第二页的数据
page2 = p.page(2)
page2.object_list
# 1url路径参数
def readbook(request,cat_id,book_id):
    content ='cat_id{}','book_id{}',cat_id,book_id
# 获取QueryDict对象
def Qd(request):
    # 获取单个字典数据
    keyword=request.GET.get('keyword')
    # 获取多个字典数据
    keyword=request.GET.getlist('keyword')
    return HttpResponse("OK")
# 表单类型数据
def formdata(request):
    data=request.POST.get()
    data=request.POST.getlist()
    return HttpResponse("OK")
# 非表单类型数据
def unform(request):
    data= request.body
    js_data = data.decode()
    import json
    dict_data = json.loads(js_data)
    print(dict_data)
    return HttpResponse('json')
def header(request):
    # 判断使用的方法
    if request.method == 'GET':
        print('GET')
    elif request.method == 'POST':
        print('POST')
    else:
        print(request.method)
        # 获取请求投中的数据
    request.META['获取的内容']
    return HttpResponse('header')


# 构造相应对象
from django.http import HttpRequest
# HttpResponse(content=响应体, content_type=响应体数据类型, status=状态码)
HttpResponse('itcast',content_type='text',status=200)
# 或者
response= HttpResponse('itcast python')
response.status_code=200
# 响应头
response['itcast']='python'


from django.http import JsonResponse
# 直接返回json数据
def jsonresponse(request):


    userinfo = {
        'user_id':123,
        'username':'itcast'
    }
    return JsonResponse(userinfo)
# 重定向
from django.shortcuts import redirect
def To_index(request):
    return redirect('/get_header')
