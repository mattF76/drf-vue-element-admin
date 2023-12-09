from rest_framework import serializers
from user.models import Account, Role, Permission


class RoleSerializerOutForAccount(serializers.ModelSerializer):
    # roleID = serializers.IntegerField(source='id')

    class Meta:
        model = Role
        # fields = '__all__'
        fields = ['id', 'roleName']


class AccountSerializerOutForQuery(serializers.ModelSerializer):
    userRoles = RoleSerializerOutForAccount(many=True)

    class Meta:
        model = Account
        # fields = '__all__'
        fields = ['id', 'username', 'realName', 'isActive', 'userRoles', 'createTime', 'updateTime']


class AccountSerializerIn(serializers.ModelSerializer):
    class Meta:
        model = Account
        # 会把请求中可以匹配上的字段数据提取出来，放到validated_data中
        fields = '__all__'


# class AccountSerializerInForDelete(serializers.ModelSerializer):
#     class Meta:
#         model = Account
#         # 会把请求中可以匹配上的字段数据提取出来，放到validated_data中
#         # fields = ['id']
#         fields = '__all__'

class PermissionSerializerOutForRole(serializers.ModelSerializer):
    # permissionID = serializers.IntegerField(source='id')

    class Meta:
        model = Permission
        # fields = '__all__'
        fields = ['id', 'permissionName']
class RoleSerializerOutForQuery(serializers.ModelSerializer):
    rolePermissions = PermissionSerializerOutForRole(many=True)
    # roleID = serializers.IntegerField(source='id')

    class Meta:
        model = Role
        fields = '__all__'

class RoleSerializerIn(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class PermissionSerializerOutForQuery(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class PermissionSerializerIn(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'