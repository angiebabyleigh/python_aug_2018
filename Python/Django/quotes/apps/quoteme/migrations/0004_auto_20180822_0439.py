# Generated by Django 2.1 on 2018-08-22 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quoteme', '0003_auto_20180822_0408'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='posted_by',
            new_name='user',
        ),
    ]
