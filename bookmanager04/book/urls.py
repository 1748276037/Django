from django.urls import path
from book.views import index,tieba_register,logiin,huoqu,set_session,RegisterView,CenterView
# 定义转换器
from django.urls import converters
class MobileConverter:
    # 定义匹配的正则
    regex='1[3-9]\d{9}'
    def to_python(self,value):
        return value
converters.register_converter(MobileConverter,'mobile')

urlpatterns = [
    path('index/',index),
    path('regist/<mobile:phone>/',tieba_register),
    path('logiin/',logiin),
    path('set_session/',set_session),
    path('register/',RegisterView.as_view()),
    path('center/',CenterView.as_view())

]
