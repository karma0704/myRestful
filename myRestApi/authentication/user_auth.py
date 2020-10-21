from rest_framework.authentication import BaseAuthentication
from rest_app01.models.token import Token
from rest_framework import exceptions


class LoginAuth(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_TOKEN', '')
        user_token = Token.objects.filter(token=token).first()
        if not user_token:
            raise exceptions.AuthenticationFailed('鉴权失败，无访问权限！')
        return user_token.account, user_token.token
