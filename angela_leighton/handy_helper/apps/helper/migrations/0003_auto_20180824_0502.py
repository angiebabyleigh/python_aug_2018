# Generated by Django 2.1 on 2018-08-24 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0002_auto_20180824_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='assigned_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='helper.User'),
        ),
        migrations.AlterField(
            model_name='job',
            name='completed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='completed', to='helper.User'),
        ),
    ]
