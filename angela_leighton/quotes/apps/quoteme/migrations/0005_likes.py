# Generated by Django 2.1 on 2018-08-22 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quoteme', '0004_auto_20180822_0439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='quoteme.Quote')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='quoteme.User')),
            ],
        ),
    ]