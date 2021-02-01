from django.db import models

# Create your models here.
from BBS.user.models import User


class Article(models.Model):

    id = models.AutoField(max_length=9, primary_key=True, verbose_name='文章ID')

    is_available = models.BooleanField(default=True, verbose_name='是否可查看')

    title = models.CharField(max_length=32, verbose_name='文章标题')

    has_img = models.BooleanField(default=False, verbose_name='有无图片')

    article_type = models.CharField(max_length=10, verbose_name='文章类型')
    # 新闻 news 体育 sports 科技 science 娱乐 entertain 文学 literature

    authority = models.BooleanField(default=False, verbose_name='文章权限')

    introduce = models.CharField(max_length=90, verbose_name='文章简介')

    content = models.TextField(verbose_name='文章内容')

    created_time = models.DateTimeField(auto_now_add=True, verbose_name='发表时间')

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    last_rank = models.IntegerField(null=True, verbose_name='上次排名')

    present_rank = models.IntegerField(null=True, verbose_name='本次排名')

    class Meta:
        db_table = 'article'


class Stars(models.Model):

    visitor = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    to_article = models.ForeignKey(Article, on_delete=models.CASCADE)

    up_time = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='评论编号')

    comment_content = models.CharField(max_length=200, verbose_name='评论详情')

    created_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')

    _parent = models.BooleanField(default=0, verbose_name='评论类型')

    publisher = models.ForeignKey(User, on_delete=models.CASCADE)

    to_log = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        db_table = 'comments'
        ordering = ['-created_time']


class Heat(models.Model):

    id = models.AutoField(max_length=99, primary_key=True)

    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    view_time = models.DateTimeField(auto_now_add=True, verbose_name='访问时间')

    visitor = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'heat'
