from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views


router = DefaultRouter()
# 默认创建的接口需要在请求末尾加/
router.register(r'users', views.UserViewSet, basename='users')

urlpatterns = [
    path('home', views.AsyncAPIView.as_view(), name='api'),
    path("func_test", views.async_view, name="func_test"),
    path("user", views.UserInfo.as_view(), name="user_info"),
    path("login", views.LoginView.as_view(), name="login"),
]

urlpatterns += router.urls