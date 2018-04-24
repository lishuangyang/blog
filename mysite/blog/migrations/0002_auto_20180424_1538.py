# Generated by Django 2.0 on 2018-04-24 07:38

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': '博客表', 'verbose_name_plural': '博客表'},
        ),
        migrations.AlterModelOptions(
            name='blogtype',
            options={'verbose_name': '类型表', 'verbose_name_plural': '类型表'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='last_updated_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=30, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='blogtype',
            name='type_name',
            field=models.CharField(max_length=50, verbose_name='类型名称'),
        ),
    ]
