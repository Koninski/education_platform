# Generated by Django 3.2 on 2023-11-12 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_auto_20231112_1816'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson', verbose_name='Урок'),
        ),
    ]
