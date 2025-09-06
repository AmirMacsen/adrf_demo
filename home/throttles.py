import random

from rest_framework.throttling import BaseThrottle


class AsyncThrottle(BaseThrottle) :

    async def allow_request(self, request, view):
        if random.random() > 0.5:
            return True
        else:
            return False
    def wait(self):
        return 3