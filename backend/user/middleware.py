import re

from .utils.jwt import parse_token
from mattAdmin.settings import NO_LOGIN_API, SUPER_ADMIN_ROLE
from .services import getRoleNamesByAccountId, getPermissionAPIsByAccountId
from django.http import JsonResponse


class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before the view (and later middleware) are called.

        # 如果请求api在NO_LOGIN_API中，则直接放行
        # if request.path in NO_LOGIN_API:
        #     response = self.get_response(request)
        #     return response
        for pattern in NO_LOGIN_API:
            if re.match(pattern, request.path):
                response = self.get_response(request)
                return response

        # 从请求头中提取token，解析用户身份
        # 请求中token为空情况
        token = request.META.get('HTTP_X_TOKEN')
        userInfo = parse_token(token)
        # 判断用户是否为空
        if userInfo.id == None:
            # a = Response({"code": 40000, "msg": "用户token错误"})  # 报错
            return JsonResponse({"code": 40000, "msg": "接口需登录才能访问"},
                            json_dumps_params={'ensure_ascii': False}, safe=False)

        #超管角色用户的请求直接放行
        role_names = getRoleNamesByAccountId(int(userInfo.id))
        if SUPER_ADMIN_ROLE in role_names:
            response = self.get_response(request)
            return response

        # 判断用户是否有权限访问当前接口
        permission_apis = getPermissionAPIsByAccountId(int(userInfo.id))
        if request.path in permission_apis:
            response = self.get_response(request)
            # Code to be executed for each request/response after the view is called.
            return response

        return JsonResponse({"code": 40000, "msg": f"当前账号无权限访问{request.path}"},
                            json_dumps_params={'ensure_ascii': False}, safe=False)

