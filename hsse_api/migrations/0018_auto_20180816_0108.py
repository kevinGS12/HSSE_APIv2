# Generated by Django 2.1 on 2018-08-16 06:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hsse_api', '0017_auto_20180806_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorrectiveAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=120)),
                ('due_date', models.DateField()),
                ('other_participants', models.CharField(max_length=60)),
                ('status', models.CharField(choices=[('OV', 'Overdue'), ('CL', 'Closed'), ('IP', 'In progress'), ('O', 'Open')], default='O', max_length=11)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CorrectiveAction_user', to=settings.AUTH_USER_MODEL)),
                ('ehhs_leader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CorrectiveAction_leader', to=settings.AUTH_USER_MODEL)),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CorrectiveAction_supervisor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control_type', models.CharField(max_length=50)),
                ('disabled', models.BooleanField()),
                ('error', models.CharField(blank=True, default='', max_length=150, null=True)),
                ('icon', models.CharField(max_length=20)),
                ('input_type', models.CharField(max_length=20)),
                ('key', models.CharField(max_length=120)),
                ('label', models.CharField(max_length=120)),
                ('options', models.CharField(blank=True, max_length=255, null=True)),
                ('order', models.IntegerField()),
                ('required', models.BooleanField()),
                ('value', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Audit_Inspection',
            new_name='AuditInspection',
        ),
        migrations.RenameModel(
            old_name='Employee_Community_Activity',
            new_name='EmployeeCommunityActivity',
        ),
        migrations.RenameModel(
            old_name='Environmental_Indicators',
            new_name='EnvironmentalIndicator',
        ),
        migrations.RenameModel(
            old_name='Monthly_Reports',
            new_name='MonthlyReport',
        ),
        migrations.RenameModel(
            old_name='Safety_Activity',
            new_name='SafetyActivity',
        ),
        migrations.RemoveField(
            model_name='corrective_action',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='corrective_action',
            name='ehhs_leader',
        ),
        migrations.RemoveField(
            model_name='corrective_action',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='corrective_action',
            name='supervisor',
        ),
        migrations.DeleteModel(
            name='Corrective_Action',
        ),
    ]