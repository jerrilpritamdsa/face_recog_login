# Generated by Django 3.0.8 on 2020-07-18 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='login_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='head_shot',
            field=models.ImageField(blank=True, upload_to='profile_images'),
        ),
    ]
