from .models import Account, Role, Permission

def getRoleNamesByAccountId(id: int) -> list[str]:
    """
    通过账号id获取账号角色列表
    @param id: 账号id
    """
    role_names = [] # 角色列表

    try:
        account = Account.objects.get(id=id)
        query_set = account.userRoles.all()
        for role in query_set:
            role_names.append(role.roleName)
    except Account.DoesNotExist as e:
        # logger.debug("账号查询不存在")
        pass
    except Role.DoesNotExist as e:
        # logger.debug("角色查询不存在")
        pass

    return role_names

#
def getPermissionAPIsByAccountId(id: int) -> list[str]:
    """
    通过账号id获取账号权限列表
    @param id: 账号id
    """
    permission_apis = set() # 接口列表

    try:
        account = Account.objects.get(id=id)
        role_query_set = account.userRoles.all()
        for role in role_query_set:
            permission_query_set = role.rolePermissions.all()
            for permssion in permission_query_set:
                permission_apis.add(permssion.permissionAPI)
    except Account.DoesNotExist as e:
        # logger.debug("账号查询不存在")
        pass
    except Role.DoesNotExist as e:
        # logger.debug("角色查询不存在")
        pass
    except Permission.DoesNotExist as e:
        # logger.debug("权限查询不存在")
        pass

    return permission_apis