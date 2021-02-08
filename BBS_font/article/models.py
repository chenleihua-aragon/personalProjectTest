from django.db import models
from user.models import User
# Create your models here.


class Article(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='文章ID')

    is_available = models.BooleanField(default=True, verbose_name='是否可查看')

    title = models.CharField(max_length=32, verbose_name='文章标题')

    article_type = models.CharField(max_length=10, verbose_name='文章类型')
    # 新闻 news 体育 sports 科技 science 娱乐 entertain 文学 literature

    introduce = models.CharField(max_length=90, verbose_name='文章简介')

    content = models.TextField(verbose_name='文章内容')

    created_time = models.DateTimeField(auto_now_add=True, verbose_name='发表时间')

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "文章名：" + str(self.title)

    class Meta:
        db_table = 'article'


class Comments(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='评论编号')

    comment_content = models.CharField(max_length=200, verbose_name='评论详情')

    created_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')

    publisher = models.ForeignKey(User, on_delete=models.CASCADE)

    to_log = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        db_table = 'comments'


class Heat(models.Model):

    id = models.AutoField(primary_key=True)

    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章标题')

    def __str__(self):
        return str(self.article.title)

    class Meta:
        db_table = 'heat'

