import re

from adrf.serializers import Serializer
from rest_framework import fields


class AsyncLoginSerializer(Serializer):
    username = fields.CharField(max_length=20)
    password = fields.CharField(max_length=20)


    def validate(self, attrs):
        username = attrs.get('username')
        pattern = re.compile(r'^[a-zA-Z0-9_-]{4,16}$')
        if not pattern.match(username):
            raise fields.ValidationError('用户名格式错误')
        else:
            return attrs


class UserSerializer(Serializer):
    username = fields.CharField(max_length=20)
    password = fields.CharField(max_length=20)
    is_active = fields.BooleanField()
    is_staff = fields.BooleanField()

