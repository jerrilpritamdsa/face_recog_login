# Generated by Django 3.0.8 on 2020-07-19 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20200719_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='login_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='logout_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
