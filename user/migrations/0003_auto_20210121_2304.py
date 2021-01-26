# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2021-01-21 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210118_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest', models.IntegerField(verbose_name='关注用户的ID')),
                ('as_friend_at', models.DateTimeField(auto_now_add=True, verbose_name='添加好友时间')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='', upload_to='avatar/'),
        ),
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='生日'),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.BooleanField(default=True, verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='user',
            name='job',
            field=models.CharField(default=' ', max_length=20, verbose_name='职业'),
        ),
        migrations.AddField(
            model_name='user',
            name='location_city',
            field=models.CharField(default=' ', max_length=22, verbose_name='城市'),
        ),
        migrations.AddField(
            model_name='user',
            name='location_province',
            field=models.CharField(default=' ', max_length=16, verbose_name='省份'),
        ),
        migrations.AddField(
            model_name='user',
            name='sign',
            field=models.CharField(default='此时无声胜有声', max_length=80, verbose_name='个性签名'),
        ),
        migrations.AddField(
            model_name='friends',
            name='master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
    ]
