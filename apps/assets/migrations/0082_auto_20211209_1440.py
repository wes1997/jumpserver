# Generated by Django 3.1.13 on 2021-12-09 06:40

from django.conf import settings
from django.db import migrations, models


def migrate_system_users_cmd_filters(apps, schema_editor):
    system_user_model = apps.get_model("assets", "SystemUser")
    cmd_filter_model = apps.get_model("assets", "CommandFilter")
    su_through = system_user_model.cmd_filters.through
    cf_through = cmd_filter_model.system_users.through

    su_relation_objects = su_through.objects.all()
    cf_relation_objects = [
        cf_through(**{
            'id': su_relation.id,
            'systemuser_id': su_relation.systemuser_id,
            'commandfilter_id': su_relation.commandfilter_id
        })
        for su_relation in su_relation_objects
    ]
    cf_through.objects.bulk_create(cf_relation_objects)


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0014_auto_20211105_1605'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assets', '0081_auto_20211105_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='commandfilter',
            name='applications',
            field=models.ManyToManyField(blank=True, related_name='cmd_filters', to='applications.Application', verbose_name='Application'),
        ),
        migrations.AddField(
            model_name='commandfilter',
            name='assets',
            field=models.ManyToManyField(blank=True, related_name='cmd_filters', to='assets.Asset', verbose_name='Asset'),
        ),
        migrations.AddField(
            model_name='commandfilter',
            name='system_users',
            field=models.ManyToManyField(blank=True, related_name='cmd_filters_pre', to='assets.SystemUser', verbose_name='System user'),
        ),
        migrations.AddField(
            model_name='commandfilter',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='cmd_filters', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='commandfilter',
            name='user_groups',
            field=models.ManyToManyField(blank=True, related_name='cmd_filters', to='users.UserGroup', verbose_name='User group'),
        ),
        migrations.AlterField(
            model_name='systemuser',
            name='cmd_filters',
            field=models.ManyToManyField(blank=True, related_name='system_users_bak', to='assets.CommandFilter', verbose_name='Command filter'),
        ),
        migrations.RunPython(migrate_system_users_cmd_filters),
        migrations.RemoveField(
            model_name='systemuser',
            name='cmd_filters',
        ),
        migrations.AlterField(
            model_name='commandfilter',
            name='system_users',
            field=models.ManyToManyField(blank=True, related_name='cmd_filters', to='assets.SystemUser', verbose_name='System user'),
        ),
    ]