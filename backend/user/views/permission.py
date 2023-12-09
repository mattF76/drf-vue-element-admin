from django.core.paginator import Paginator

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.models import Permission
from user.serializers import PermissionSerializerOutForQuery, PermissionSerializerIn

from utils.log import logger


@api_view(['POST'])
def query(request):
    """
    查询角色列表
    """
    query_set = Permission.objects.all()

    # 多条件查询
    permissionName = request.data.get('permissionName', None)
    if permissionName:
        query_set = query_set.filter(permissionName__contains=permissionName)

    permissionAPI = request.data.get('permissionAPI', None)
    if permissionAPI:
        query_set = query_set.filter(permissionAPI__contains=permissionAPI)

    # 分页
    pageSize = request.query_params['pageSize']  # 每页显示的结果数量
    currentPage = request.query_params['currentPage']  # 每页显示的结果数量
    paginator = Paginator(query_set, pageSize)
    page = paginator.get_page(currentPage)

    # 将查询结果转化为需要的格式，例如JSON
    data = [PermissionSerializerOutForQuery(item).data for item in page]

    # 构建包含分页信息的JSON响应
    response_data = {
        'total': paginator.count,
        'items': data,
    }

    return Response({"code": 20000, "msg": "权限查询成功", "data": response_data})


@api_view(['POST'])
def add(request):
    """
    账号添加
    """
    # 请求参数校验
    serializer = PermissionSerializerIn(data=request.data)
    if not serializer.is_valid():
        # print(serializer.errors)
        return Response({"code": 40000, "msg": f"请求参数错误: {serializer.errors}"})
    # logger.debug(f"serializer.validated_data: {serializer.validated_data}")

    # 实例添加
    serializer.save()
    return Response({"code": 20000, "msg": f"权限添加成功"})

@api_view(['POST'])
def delete(request):
    """
    账号删除
    """
    # 请求参数校验
    # 检查request.data是list
    # 遍历list，确保其元素是dict
    # 确保dict元素有id键
    try:
        assert isinstance(request.data, list), "请求参数不是list类型"
        assert len(request.data) > 0, "请求参数list长度不大于0"
        for item in request.data:
            assert isinstance(item, dict), "请求参数list中元素不是dict类型"
            id = item.get('id', None)
            if id is not None:
                Permission.objects.get(id=int(id)).delete()
            else:
                raise Exception("请求参数中不含角色id")
    except Exception as e:
        return Response({"code": 40000, "msg": f"权限删除失败: {e}"})

    return Response({"code": 20000, "msg": f"权限删除成功"})


@api_view(['POST'])
def update(request):
    """
    账号修改接口
    """
    id = request.data["id"]
    if not id:
        return Response({"code": 40000, "msg": "更新失败：id值为空"})
    role = Permission.objects.get(id=int(id))

    # 请求参数校验
    serializer = PermissionSerializerIn(role, data=request.data)
    if not serializer.is_valid():
        return Response({"code": 40000, "msg": f"请求参数错误: {serializer.errors}"})
    # logger.debug(f"serializer.validated_data: {serializer.validated_data}")

    # 实例修改
    serializer.save()
    return Response({"code": 20000, "msg": f"权限修改成功"})
#
