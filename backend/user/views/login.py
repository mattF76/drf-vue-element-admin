from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.models import Account
from user.services import getRoleNamesByAccountId

from utils.log import logger
from user.utils.jwt import UserInfo, generate_token, parse_token


@api_view(['POST'])
def login(request):
    """
    登录接口
    """
    query_set = Account.objects.all()

    # 多条件查询
    username = request.data['username']
    password = request.data['password']

    if (not username) or (not password):
        return Response({"code": 40000, "msg": "账号或密码不能为空"})

    query_set = query_set.filter(username = username).filter(password = password)
    if query_set.count() == 1:
        user = query_set.first()

        # 生成用户对应token
        userInfo = UserInfo(id=user.id, username=user.username)
        token = generate_token(userInfo)
        return Response({"code": 20000, "msg": "登录成功", "data": {"token": token}})
    else:
        return Response({"code": 40000, "msg": "账号或密码错误"})


@api_view(['POST'])
def logout(request):
    """
    登出接口
    """
    return Response({"code": 20000, "msg": f"推出登录成功"})

@api_view(['GET'])
def info(request):
    """
    查询账号信息，返回账号角色
    """
    query_set = Account.objects.all()
    # token = request.data['token']
    token = request.query_params.get('token', None)

    if (not token):
        return Response({"code": 40000, "msg": "请求中token为空"})

    userInfo = parse_token(token)
    # 判断用户是否为空
    if userInfo.id == None:
        # a = Response({"code": 40000, "msg": "用户token错误"})  # 报错
        return Response({"code": 40000, "msg": "token无效"})

    # 超管角色用户的请求直接放行
    role_names = getRoleNamesByAccountId(int(userInfo.id))
    if len(role_names) > 0:
        return Response({
            "code": 20000,
            "msg": "查询账号信息成功",
            'data':{
                'roles': role_names,
                'introduction': 'I am an user',
                'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
                'name': 'Normal Editor'
            }
        })
    else:
        Response({"code": 40000, "msg": "查询账号角色失败"})
