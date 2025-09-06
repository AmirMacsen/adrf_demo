import random


class AsyncPermission:
    """
    权限校验
    """
    async def has_permission(self, request, view):
        if random.random() > 0.5:
            return True

    async def has_object_permission(self, request, view, obj):
        if random.random() > 0.5:
            return True