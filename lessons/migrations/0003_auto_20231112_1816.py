# Generated by Django 3.2 on 2023-11-12 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='overall_rating',
        ),
        migrations.AddField(
            model_name='lesson',
            name='likes_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Количество лайков'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson', verbose_name='Урок'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.TextField(max_length=2000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название урока'),
        ),
    ]