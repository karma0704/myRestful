from rest_app01.models.account import Account
from rest_app01.models.token import Token
from rest_framework.views import APIView
from django.http import JsonResponse
from hashlib import sha1
from time import time


def make_password(password):
    """
    sha1密码加密的方法
    :param password:
    :return:
    """
    return sha1(password.encode('utf-8')).hexdigest()


def get_random_str(user):
    """
    字符串使用sha1进行加盐加密
    :param user:
    :return:
    """
    auth_str = user + str(time())
    return sha1(auth_str.encode('utf-8')).hexdigest()


class LoginView(APIView):
    authentication_classes = []
    def post(self, request, *args, **kwargs):
        print(request.data)
        nickname = request.data.get('nickname', '')
        password = request.data.get('password', '')
        passwd = make_password(str(password))
        res = {'status_code': 1000, 'msg': ''}
        if all([nickname, password]):
            user = Account.objects.filter(nickname=str(nickname), password=passwd).first()
            print(user)
            if not user:
                res['status_code'], res['msg'] = 1001, '用户名或密码错误！'
                return JsonResponse(res, safe=False)
            res['msg'] = '登录成功！'
            res['token'] = get_random_str(user.nickname)
            Token.objects.update_or_create(account=user, defaults={'token': get_random_str(user.nickname)})
            return JsonResponse(res, safe=False)
        if not nickname:
            res['status_code'], res['msg'] = 1001, '用户名不能为空！'
            return JsonResponse(res, safe=False)
        if not password:
            res['status_code'], res['msg'] = 1001, '用户密码不能为空！'
            return JsonResponse(res, safe=False)
