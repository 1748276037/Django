from django.db import models

# Create your models here.
class BookInfo(models.Model):
    # id自动生成
    name = models.CharField(max_length=10)
    def __str__(self):
        return  self.name
class NameInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField(max_length=10)
    # 主键删除从键一起消失
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)