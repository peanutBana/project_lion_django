# Generated by Django 4.0.4 on 2022-04-29 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demos', '0003_alter_comment_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_ad',
            new_name='created_at',
        ),
    ]
