from django.db import models
from rest_app01.models.account import Account


class Token(models.Model):
    token = models.CharField(verbose_name='token', max_length=64)
    account = models.ForeignKey(verbose_name='用户', to=Account, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.token

    class Meta:
        db_table = 'ra_user_token'
        verbose_name = '用户认证'
        verbose_name_plural = verbose_name
