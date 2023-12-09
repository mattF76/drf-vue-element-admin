from django.urls import path

# from . import views
from user.views import account, role, permission, login

app_name = "user"
urlpatterns = [
    # 账号相关接口
    path("account/list", account.query, name="account_query"),
    path("account/add", account.add, name="account_add"),
    path("account/del", account.delete, name="account_del"),
    path("account/update", account.update, name="account_update"),
    # 角色相关接口
    path("role/list", role.query, name="role_query"),
    path("role/add", role.add, name="role_add"),
    path("role/del", role.delete, name="role_del"),
    path("role/update", role.update, name="role_update"),
    # 权限相关接口
    path("permission/list", permission.query, name="permission_query"),
    path("permission/add", permission.add, name="permission_add"),
    path("permission/del", permission.delete, name="permission_del"),
    path("permission/update", permission.update, name="permission_update"),
    # 账号登录接口
    path("login", login.login, name="login"),
    path("logout", login.logout, name="logout"),
    path("info", login.info, name="info"),
]