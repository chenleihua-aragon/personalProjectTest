# Generated by Django 3.1.5 on 2021-02-08 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_delete_stars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='_parent',
        ),
    ]