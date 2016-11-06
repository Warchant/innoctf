# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    title = models.CharField(max_length=1024, verbose_name='Заголовок')
    date_published = models.DateTimeField()
    content = models.TextField(max_length=10000, verbose_name='Текст статьи')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Автор')

    def __unicode__(self):
        return self.title[:255]