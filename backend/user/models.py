from django.db import models


class Permission(models.Model):
    """权限"""
    permissionName = models.CharField(verbose_name="权限名", max_length=200, unique=True)
    permissionAPI = models.CharField(verbose_name="接口", max_length=200, blank=True)
    createTime = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updateTime = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    def __str__(self):
        return f"权限id: {self.id}，权限名: {self.permissionName}，接口: {self.permissionName}"

    class Meta:
        ordering = ['createTime']


class Role(models.Model):
    """角色"""
    roleName = models.CharField(verbose_name="角色名", max_length=20, unique=True)
    roleNote = models.CharField(verbose_name="角色说明", max_length=200, blank=True)
    rolePermissions = models.ManyToManyField(Permission, blank=True)
    createTime = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updateTime = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    def __str__(self):
        return f"角色ID：{self.id}, 角色: {self.roleName}，说明: {self.roleNote}"

    class Meta:
        ordering = ['createTime']


class Account(models.Model):
    """用户"""
    username = models.CharField(verbose_name="账号名", max_length=20, unique=True)
    realName = models.CharField(verbose_name="姓名", max_length=50, blank=True)
    password = models.CharField(verbose_name="密码", max_length=100, blank=True)
    isActive = models.BooleanField(verbose_name="账号状态", default=True)
    userRoles = models.ManyToManyField(Role, blank=True)
    createTime = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updateTime = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    def __str__(self):
        return f"账号id: {self.id}, 账号: {self.username}，姓名: {self.realName}，启用: {self.isActive}"

    class Meta:
        ordering = ['createTime']
