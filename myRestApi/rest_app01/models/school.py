from django.db import models
from django.contrib.auth.models import *


class School(models.Model):
    avatar = models.ImageField(verbose_name='学校logo', upload_to='images/%Y_%m_%d')
    name = models.CharField(verbose_name='学校名字', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ra_schools'
        verbose_name = '学校管理'
        verbose_name_plural = verbose_name
