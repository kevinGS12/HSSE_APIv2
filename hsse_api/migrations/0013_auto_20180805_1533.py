# Generated by Django 2.0.7 on 2018-08-05 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hsse_api', '0012_auto_20180804_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hsse_api.Site'),
        ),
    ]
