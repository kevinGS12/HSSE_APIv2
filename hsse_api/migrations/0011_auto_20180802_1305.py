# Generated by Django 2.0.7 on 2018-08-02 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hsse_api', '0010_auto_20180802_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environmental_indicators',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='environmental_indicators', to='hsse_api.Site'),
        ),
    ]
