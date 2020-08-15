from django.db import models

# Create your models here.
class BookInfo(models.Model):
    name = models.CharField(max_length=10)
                        # 日期 不能为空
    pub_date = models.DateField(null=True)
                        # 整数不为0
    readcount = models.IntegerField(default=0)
                         # 整数不为0
    commentcount = models.IntegerField(default=0)
                        # 布尔字默认
    is_delete =models.BooleanField(default=False)
    # 设置表明
    class Meta:
        db_table = 'bookinfo'
        verbose_name = 'Admin站点里显示'

    def __str__(self):

            return self.name
class PeopleInfo(models.Model):
    # 枚举
    GENDER_CHOICE={
        (0,'male'),
        (1, 'female')
    }
    name = models.CharField(max_length=10)
    gender =models.SmallIntegerField(choices=GENDER_CHOICE,default=0)
    description = models.CharField(max_length=100)
    is_delete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = 'Admin站点里显示'

    def __str__(self):
        return self.name
