from django.contrib import admin

# Register your models here.
from .models import Account, Role, Permission

admin.site.register(Account)
admin.site.register(Role)
admin.site.register(Permission)