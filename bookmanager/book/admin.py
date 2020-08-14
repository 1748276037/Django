from django.contrib import admin

# Register your models here.
# 注册模型类
from book.models import BookInfo,NameInfo
admin.site.register(BookInfo)
admin.site.register(NameInfo)