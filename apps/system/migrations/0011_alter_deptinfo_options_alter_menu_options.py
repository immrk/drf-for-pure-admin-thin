# Generated by Django 5.1 on 2024-10-31 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0010_menu_redirect'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deptinfo',
            options={'ordering': ('rank', 'create_time'), 'verbose_name': '部门表', 'verbose_name_plural': '部门表'},
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ('create_time',), 'verbose_name': '菜单/权限表', 'verbose_name_plural': '菜单/权限表'},
        ),
    ]
