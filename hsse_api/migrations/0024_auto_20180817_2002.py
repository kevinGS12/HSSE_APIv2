# Generated by Django 2.1 on 2018-08-18 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hsse_api', '0023_auto_20180816_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date_reported',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='report',
            name='first_day_lost',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='report',
            name='restricted_activity_start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='report',
            name='return_work_date',
            field=models.DateField(),
        ),
    ]
