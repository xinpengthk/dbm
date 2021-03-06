# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-17 11:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrdBusiness',
            fields=[
                ('businessId', models.BigAutoField(db_column='business_id', help_text='主键自增ID', primary_key=True, serialize=False, verbose_name='主键ID')),
                ('businessName', models.CharField(db_column='business_name', help_text='请输入业务线名称!', max_length=32, unique=True, verbose_name='业务线名称')),
                ('businessStatus', models.SmallIntegerField(choices=[(0, '未上线'), (1, '已上线'), (2, '已下线')], db_column='business_status', default=1, help_text='业务线状态，0：未上线，1：已上线，2：已下线', verbose_name='业务线状态')),
                ('businessDesc', models.EmailField(db_column='business_desc', help_text='业务线描述！', max_length=128, verbose_name='业务线描述')),
                ('isDel', models.SmallIntegerField(choices=[(0, '未删除'), (1, '已删除')], db_column='is_del', default=0, help_text='该记录是否被删除，0：未删除，1：已删除，默认为0', verbose_name='该记录是否被删除')),
                ('createdTime', models.DateTimeField(auto_now_add=True, db_column='created_time', help_text='该记录创建时间', null=True, verbose_name='记录创建时间')),
                ('updatedTime', models.DateTimeField(auto_now=True, db_column='updated_time', help_text='记录最后更新时间', null=True, verbose_name='记录最后更新时间')),
            ],
            options={
                'verbose_name': '业务线表',
                'verbose_name_plural': '业务线表',
                'db_table': 'prd_business',
            },
        ),
        migrations.CreateModel(
            name='PrdProduct',
            fields=[
                ('productId', models.BigAutoField(db_column='product_id', help_text='主键自增ID', primary_key=True, serialize=False, verbose_name='主键ID')),
                ('productName', models.CharField(db_column='product_name', db_index=True, help_text='请输入产品线名称!', max_length=32, verbose_name='产品线名称')),
                ('productStatus', models.SmallIntegerField(choices=[(0, '未上线'), (1, '已上线'), (2, '已下线')], db_column='product_status', default=1, help_text='产品线状态，0：未上线，1：已上线，2：已下线', verbose_name='产品线状态')),
                ('productDesc', models.EmailField(db_column='product_desc', help_text='产品线描述！', max_length=128, verbose_name='产品线描述')),
                ('isDel', models.SmallIntegerField(choices=[(0, '未删除'), (1, '已删除')], db_column='is_del', default=0, help_text='该记录是否被删除，0：未删除，1：已删除，默认为0', verbose_name='该记录是否被删除')),
                ('createdTime', models.DateTimeField(auto_now_add=True, db_column='created_time', help_text='该记录创建时间', null=True, verbose_name='记录创建时间')),
                ('updatedTime', models.DateTimeField(auto_now=True, db_column='updated_time', help_text='记录最后更新时间', null=True, verbose_name='记录最后更新时间')),
                ('businessId', models.ForeignKey(db_column='business_id', db_index=False, help_text='请选择业务线', on_delete=django.db.models.deletion.DO_NOTHING, to='business.PrdBusiness', verbose_name='业务线编号，外键')),
            ],
            options={
                'verbose_name': '产品线表',
                'verbose_name_plural': '产品线表',
                'db_table': 'prd_product',
            },
        ),
        migrations.CreateModel(
            name='PrdService',
            fields=[
                ('serviceId', models.BigAutoField(db_column='service_id', help_text='主键自增ID', primary_key=True, serialize=False, verbose_name='主键ID')),
                ('serviceName', models.CharField(db_column='service_name', db_index=True, help_text='请输入服务名称！', max_length=32, verbose_name='服务名称')),
                ('serviceStatus', models.SmallIntegerField(choices=[(0, '未上线'), (1, '已上线'), (2, '已下线')], db_column='service_status', default=1, help_text='服务状态，0：未上线，1：已上线，2：已下线', verbose_name='服务状态，0：未上线，1：已上线，2：已下线')),
                ('serviceDesc', models.EmailField(db_column='service_desc', help_text='服务描述！', max_length=128, verbose_name='服务描述')),
                ('isDel', models.SmallIntegerField(choices=[(0, '未删除'), (1, '已删除')], db_column='is_del', default=0, help_text='该记录是否被删除，0：未删除，1：已删除，默认为0', verbose_name='该记录是否被删除')),
                ('createdTime', models.DateTimeField(auto_now_add=True, db_column='created_time', help_text='该记录创建时间', null=True, verbose_name='记录创建时间')),
                ('updatedTime', models.DateTimeField(auto_now=True, db_column='updated_time', help_text='记录最后更新时间', null=True, verbose_name='记录最后更新时间')),
                ('productId', models.ForeignKey(db_column='product_id', db_index=False, help_text='请选择产品线', on_delete=django.db.models.deletion.DO_NOTHING, related_name='product_id', to='business.PrdProduct', verbose_name='产品线编号，外键')),
                ('serviceDevLedear', models.ForeignKey(db_column='service_dev_ledear', db_index=False, help_text='请选择该服务开发ledear！', on_delete=django.db.models.deletion.DO_NOTHING, related_name='serviceDevLedear', to='account.SysUser', verbose_name='该服务开发ledear，外键, sys_user')),
                ('servicePdm', models.ForeignKey(db_column='service_pdm', db_index=False, help_text='请选择项目经理！', on_delete=django.db.models.deletion.DO_NOTHING, related_name='servicePdm', to='account.SysUser', verbose_name='该服务项目经理id，外键, sys_user')),
                ('servicePjm', models.ForeignKey(db_column='service_pjm', db_index=False, help_text='请选择产品经理！', on_delete=django.db.models.deletion.DO_NOTHING, related_name='servicePjm', to='account.SysUser', verbose_name='该服务产品经理id，外键, sys_user')),
                ('serviceQaLedear', models.ForeignKey(db_column='service_qa_ledear', db_index=False, help_text='请选择该服务测试ledear！', on_delete=django.db.models.deletion.DO_NOTHING, related_name='serviceQaLedear', to='account.SysUser', verbose_name='该服务测试ledear，外键, sys_user')),
            ],
            options={
                'verbose_name': '产品线中服务表',
                'verbose_name_plural': '产品线中服务表',
                'db_table': 'prd_service',
            },
        ),
    ]
