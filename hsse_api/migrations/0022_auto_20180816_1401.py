# Generated by Django 2.1 on 2018-08-16 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hsse_api', '0021_auto_20180816_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='key',
            field=models.CharField(max_length=120),
        ),
    ]
