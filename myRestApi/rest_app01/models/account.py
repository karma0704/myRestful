from django.db import models


class Account(models.Model):
    ROLE_CHOICES = (
        (1, '普通用户'),
        (2, '白银会员'),
        (3, '黄金会员'),
        (4, '白金会员'),
        (5, '钻石会员'),
        (6, '超级管理员'),
    )
    nickname = models.CharField(verbose_name='用户昵称', unique=True, blank=False, max_length=30, null=False)
    password = models.CharField(verbose_name='用户密码', blank=False, max_length=40, null=False)
    phone = models.CharField(verbose_name='电话号码', blank=False, max_length=11, null=False)
    email = models.CharField(verbose_name='电子邮箱', blank=True, max_length=30, null=True)
    role = models.IntegerField(verbose_name='用户角色', choices=ROLE_CHOICES, default=1)
    avatar = models.ImageField(verbose_name='头像', null=True, upload_to='images/user/avatars')
    logintimes = models.IntegerField(verbose_name='登录次数', default=0)
    last_login_time = models.DateTimeField(auto_now=True)
    mark = models.CharField(verbose_name='用户备注', max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nickname

    class Meta:
        db_table = 'ra_accounts'
        verbose_name = '用户管理'
        verbose_name_plural =  verbose_name
