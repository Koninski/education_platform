# Generated by Django 3.2 on 2023-11-07 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20231104_0815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='nikname',
            new_name='username',
        ),
    ]
