# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-14 22:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_sysgroup_sysgrouprole_sysgroupservice_sysmenu_sysrole_sysrolemenu_sysusergroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sysgroup',
            name='groupStatus',
            field=models.SmallIntegerField(choices=[(0, '不可用'), (1, '可用')], db_column='group_status', default=1, help_text='项目组状态，0：不可用，1：可用', verbose_name='项目组状态'),
        ),
        migrations.AlterField(
            model_name='sysgrouprole',
            name='groupId',
            field=models.ForeignKey(help_text='用户组 ID', on_delete=django.db.models.deletion.CASCADE, to='account.SysGroup', verbose_name='用户组 ID'),
        ),
        migrations.AlterField(
            model_name='sysgrouprole',
            name='roleId',
            field=models.ForeignKey(help_text='角色 ID', on_delete=django.db.models.deletion.CASCADE, to='account.SysRole', verbose_name='角色 ID'),
        ),
        migrations.AlterField(
            model_name='sysgroupservice',
            name='groupId',
            field=models.ForeignKey(help_text='用户组 ID', on_delete=django.db.models.deletion.CASCADE, to='account.SysGroup', verbose_name='用户组 ID'),
        ),
        migrations.AlterField(
            model_name='sysgroupservice',
            name='serviceId',
            field=models.ForeignKey(help_text='服务 ID', on_delete=django.db.models.deletion.CASCADE, to='business.PrdService', verbose_name='服务 ID'),
        ),
        migrations.AlterField(
            model_name='sysrolemenu',
            name='menuId',
            field=models.BigIntegerField(db_column='menu_id', help_text='菜单 ID', verbose_name='菜单 ID'),
        ),
        migrations.AlterField(
            model_name='sysrolemenu',
            name='roleId',
            field=models.BigIntegerField(db_column='role_id', help_text='角色 ID', verbose_name='角色 ID'),
        ),
        migrations.AlterField(
            model_name='sysusergroup',
            name='groupId',
            field=models.BigIntegerField(db_column='group_id', help_text='用户组 ID', verbose_name='用户组 ID'),
        ),
        migrations.AlterField(
            model_name='sysusergroup',
            name='userId',
            field=models.BigIntegerField(db_column='user_id', help_text='用户 ID', verbose_name='用户 ID'),
        ),
    ]