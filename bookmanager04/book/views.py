from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('ok ')

def tieba_register(request,phone):
    return HttpResponse(phone)

# 设置cookie
def logiin(request):
    username=request.GET.get('username')
    response = HttpResponse('123')
    response.set_cookie(key='username', value=username, max_age=10000)
    return response
# 获取cookie
def huoqu(request):
    cookie1 = request.COOKIES.get('username')
    print(cookie1)
    return HttpResponse(cookie1)


def set_session(request):
    # 1. 设置session
    # request.session['user_id']=123456789
    # 2根据键读取值。
    # user_id = request.session.get('user_id')

    # 清除所有session，只是删除session内容,key保留。
    # request.session.clear()
    # 删除session的数据, 同时把sesion的key也删除
    # request.session.flush()
    # 根据key删除
    del request.session['键']
    return HttpResponse('okk')

from django.views import View
class RegisterView(View):
    # get方式请求
    def get(self,request):
        return HttpResponse('view get')
    # post方式请求
    def post(self,request):
        return HttpResponse('view post')

from django.contrib.auth.mixins import LoginRequiredMixin
# 判断用户是否登录
class CenterView(LoginRequiredMixin,View):
    # get方式请求
    def get(self, request):
        return HttpResponse('view get')

    # post方式请求
    def post(self, request):
        return HttpResponse('view post')
