from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('ok')

from book.models import BookInfo,PeopleInfo
# 增加数据
book = BookInfo(
    name= 'itcast',
    pub_date='2010-4-5'
)
book.save()
# 方式2
book = BookInfo.objects.create(
    name = 'cast',
    )

# 修改
person = PeopleInfo.objects.get(name = '黄药师')
person.name = 'itcast'
person.save()
# 方式2
PeopleInfo.objects.filter(name='itcast').update(name='船只博客')


# 删除
# 方式1物理删除
book = BookInfo.objects.get(id=6)
book.delete()

# 方式2
BookInfo.objects.filter(id=5).delete()

# 查询f
# filter过滤出多个结果
# exclude排除掉符合条件剩下的结果
# get过滤单一结果
# all查询多个结果。 查询结果集 -- 实际就是一个列表
# count查询结果数量。
BookInfo.objects.get(id=1).name
BookInfo.objects.all()
BookInfo.objects.all().count()

# 相等查询
BookInfo.objects.filter(id=1)
# 模糊查询 contains
BookInfo.objects.filter(name__contains='传')
# startswith、endswith：以指定值开头或结尾。
BookInfo.objects.filter(name__endswith='部')
BookInfo.objects.filter(name__startswith='天')
# in：是否包含在范围内。
BookInfo.objects.filter(id__in=[1,3,5])
# 比较查询
# gt大于 (greater then)
# gte大于等于 (greater then equal)
# lt小于 (less then)
# lte小于等于 (less then equal)
BookInfo.objects.filter(id__gt=1)
# year、month、day、week_day、hour、minute、second：对日期时间类型的属性进行运算。
BookInfo.objects.filter(pub_date__year=1980)

from django.db.models import F
from django.db.models import Q
# F用于属性之间的比较
BookInfo.objects.filter(readcount__gt=F('commentcount'))
# Q用表示逻辑与关系，同sql语句中where部分的and关键字。
# 查询阅读量大于20，并且编号小于3的图书
BookInfo.objects.filter(readcount__gt=20,id__lt=3)

# 查询阅读量大于20，或编号小于3的图书，只能使用Q对象实现
BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))
# Q对象前可以使用~操作符，表示非not
BookInfo.objects.filter(~Q(id=3))


# 一对应的模型类对象.多对应的模型类名小写_set 例：
book = BookInfo.objects.get(id=1)
book.peopleinfo_set.all()

# 由多到一的访问语法:
# 多对应的模型类对象.多对应的模型类中的关系类属性名 例：
peson=PeopleInfo.objects.get(id=1)
person.book

# 查询图书，要求图书人物为"郭靖"
book = BookInfo.objects.filter(peopleinfo__name='郭靖')
# 查询人物为1的书籍信息
person=PeopleInfo.objects.get(id=1)
person.book.name
# 或者
book = BookInfo.objects.filter(peopleinfo__id=1)