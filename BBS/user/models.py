from django.db import models

# Create your models here.


class User(models.Model):

    name = models.CharField(max_length=12, primary_key=True, verbose_name='用户名')

    is_active = models.BooleanField(default=True, verbose_name='是否可用')

    password = models.CharField(max_length=32, verbose_name='密码')

    avatar = models.ImageField(upload_to='avatar/', default='')

    sign = models.CharField(max_length=80, default='此时无声胜有声', verbose_name='个性签名')

    location_province = models.CharField(max_length=16, default=' ', verbose_name='省份')

    location_city = models.CharField(max_length=22, default=' ', verbose_name='城市')

    gender = models.BooleanField(default=True, verbose_name='性别')

    birthday = models.DateField(blank=True, null=True, verbose_name='生日')

    job = models.CharField(max_length=20, default=' ', verbose_name='职业')

    last_news = models.IntegerField(default=0, verbose_name='上次访问时公开新闻类ID')

    last_sports = models.IntegerField(default=0, verbose_name='上次访问时公开体育类ID')

    last_science = models.IntegerField(default=0, verbose_name='上次访问时公开科学类ID')

    last_entertain = models.IntegerField(default=0, verbose_name='上次访问时公开娱乐类ID')

    last_literature = models.IntegerField(default=0, verbose_name='上次访问时公开文学类ID')

    inform_comment = models.DateTimeField(default='', verbose_name='上次查看评论我的时间')

    inform_reply = models.DateTimeField(default='', verbose_name='上次查看回复我的时间')

    inform_up = models.DateTimeField(default='', verbose_name='上次查看点赞我的时间')

    inform_follow = models.DateTimeField(default='', verbose_name='上次查看关注我的时间')

    created_time = models.DateTimeField(auto_now_add=True, verbose_name='账户创建时间')

    modified_time = models.DateTimeField(auto_now_add=True, verbose_name='修改时间')

    class Meta:
        db_table = 'u_s_e_r'


class Friends(models.Model):

    master = models.ForeignKey(User)

    guest = models.IntegerField(null=False, verbose_name='关注用户的ID')

    as_friend_at = models.DateTimeField(auto_now_add=True, verbose_name="添加好友时间")
