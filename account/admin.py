from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from account.entity.SysDept import SysDept
from account.entity.SysGroup import SysGroup
from account.entity.SysGroupRole import SysGroupRole
from account.entity.SysGroupService import SysGroupService
from account.entity.SysMenu import SysMenu
from account.entity.SysRole import SysRole
from account.entity.SysRoleMenu import SysRoleMenu
from account.entity.SysTitle import SysTitle
from account.entity.SysUser import SysUser
from account.entity.SysUserGroup import SysUserGroup

class SysUserForm(forms.ModelForm):
    class Meta:
        model = SysUser
        fields = '__all__'
    widgets = {
            'userPwd' : forms.PasswordInput(),
        }

class SysUserAdmin(admin.ModelAdmin):
    form = SysUserForm
    list_display = ('userName', 'userEmail', 'userPhone', 'userStatus')
    list_per_page=30
    

admin.site.register(SysDept)
admin.site.register(SysTitle)
admin.site.register(SysUser, SysUserAdmin)
admin.site.register(SysGroup)
admin.site.register(SysGroupRole)
admin.site.register(SysGroupService)
admin.site.register(SysMenu)
admin.site.register(SysRole)
admin.site.register(SysRoleMenu)
admin.site.register(SysUserGroup)


