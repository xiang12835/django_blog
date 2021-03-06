# coding=utf-8
from __future__ import unicode_literals

# from django.db import models

# # Create your models here.

# class Mysite(models.Model):
# 	title = models.CharField(max_length=100)
# 	url = models.URLField()
# 	author = models.CharField(max_length=100)
# 	num = models.IntegerField(max_length=10)


from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):  # __str__ on Python 3
        return self.name

class Tag(models.Model):
    tag_name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.tag_name

class Article(models.Model):
    title = models.CharField(max_length=100)  # 博客题目
    category = models.ForeignKey(Category, blank=True)  # 博客分类
    tag = models.ManyToManyField(Tag, blank=True)  # 博客标签 可为空
    date_time = models.DateTimeField(auto_now_add=True)  # 博客日期
    content = models.TextField(blank=True, null=True)  # 博客文章正文

    # 获取URL并转换成url的表示格式
    def get_absolute_url(self):
        path = reverse('article', args=[self.id])
        return "http://www.flyingfish.online%s" % path

    def __unicode__(self):
        return self.title

    class Meta:  # 按时间下降排序
        ordering = ['-date_time']