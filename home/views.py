from adrf.decorators import api_view
from adrf.views import APIView # 使用adrf的库实现
from adrf.viewsets import ViewSet
from django.contrib.auth import get_user_model, aauthenticate
from django.http import JsonResponse

from home.permissions import AsyncPermission
from home.serializers import AsyncLoginSerializer, UserSerializer
from home.throttles import AsyncThrottle

User = get_user_model()

class AsyncAPIView(APIView):
    async def get(self, request):
        return JsonResponse({"message": "Hello World"})


@api_view(["GET"])  # 使用adrf中的装饰器实现
async def async_view(request):
    return JsonResponse({"message": "Hello async func view"})


class UserInfo(APIView):
    # permission_classes = [AsyncPermission]
    throttle_classes = [AsyncThrottle]
    async def get(self, request):
        return JsonResponse({"message": "Hello World"})


class UserViewSet(ViewSet):
    async def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        users = await serializer.adata
        return JsonResponse({"message": "异步UserList视图集", "users": users})

    async def retrieve(self, request, pk):
        user = await User.objects.afirst()
        return JsonResponse({"message": "异步UserRetrive视图集", "username": user.username})


class LoginView(APIView):

    async def post(self, request):
        serializer = AsyncLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = await aauthenticate(request, **serializer.validated_data)
            user_serializer = UserSerializer(user)
            user_dict = await user_serializer.adata
            return JsonResponse({"message": "登录成功", "user": user_dict})
        return JsonResponse({"message": "登录失败", "errors": serializer.errors})