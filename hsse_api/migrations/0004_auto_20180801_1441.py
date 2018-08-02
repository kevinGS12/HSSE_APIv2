# Generated by Django 2.0.7 on 2018-08-01 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hsse_api', '0003_auto_20180801_0139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audit_inspection',
            old_name='user',
            new_name='made_by',
        ),
        migrations.RemoveField(
            model_name='corrective_action',
            name='ehhs',
        ),
        migrations.RemoveField(
            model_name='corrective_action',
            name='user',
        ),
        migrations.RemoveField(
            model_name='report',
            name='user',
        ),
        migrations.AddField(
            model_name='corrective_action',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='corrective_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='corrective_action',
            name='ehhs_leader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='corrective_leader', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='employee_community_activity',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='report',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='corrective_action',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='corrective_action',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='corrective_supervisor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='report',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report_approver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='report',
            name='ehhs_leader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report_leader', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='report',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report_supervisor', to=settings.AUTH_USER_MODEL),
        ),
    ]
