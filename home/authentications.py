from django.contrib.auth import get_user_model
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header

User = get_user_model()

class AsyncAuthentication(BaseAuthentication):
    keyword = "JWT"
    async def authenticate(self, request):
        # 从Authorization 中获取 Authorization: JWT XXX
        auth = get_authorization_header(request).split()
        token = auth[1].decode('utf-8')
        if token == '1234':
            user = await User.objects.afirst()
            setattr(request, 'user', user)
            return user, None
        else:
            raise exceptions.AuthenticationFailed('Invalid token')