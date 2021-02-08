from django.db import models

# Create your models here.


class User(models.Model):

    name = models.CharField(max_length=12, primary_key=True, verbose_name='用户名')

    is_active = models.BooleanField(default=True, verbose_name='是否可用')

    password = models.CharField(max_length=32, verbose_name='密码')

    sign = models.CharField(max_length=80, default='此时无声胜有声', verbose_name='个性签名')

    location_province = models.CharField(max_length=16, default=' ', verbose_name='省份')

    location_city = models.CharField(max_length=22, default=' ', verbose_name='城市')

    gender = models.BooleanField(default=True, verbose_name='性别')

    birthday = models.DateField(blank=True, null=True, verbose_name='生日')

    job = models.CharField(max_length=20, default=' ', verbose_name='职业')

    created_time = models.DateTimeField(auto_now_add=True, verbose_name='账户创建时间')

    modified_time = models.DateTimeField(auto_now_add=True, verbose_name='修改时间')

    class Meta:
        db_table = 'u_s_e_r'
