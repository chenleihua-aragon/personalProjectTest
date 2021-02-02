# Generated by Django 3.1.5 on 2021-02-01 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='inform_comment',
            field=models.DateTimeField(blank=True, null=True, verbose_name='上次查看评论我的时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='inform_follow',
            field=models.DateTimeField(blank=True, null=True, verbose_name='上次查看关注我的时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='inform_reply',
            field=models.DateTimeField(blank=True, null=True, verbose_name='上次查看回复我的时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='inform_up',
            field=models.DateTimeField(blank=True, null=True, verbose_name='上次查看点赞我的时间'),
        ),
    ]