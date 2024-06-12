# Generated by Django 4.2.13 on 2024-06-12 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_levels', '0002_rpv5_rpv6_rpv7_delete_waterlevel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rpv5',
            name='name',
        ),
        migrations.RemoveField(
            model_name='rpv6',
            name='name',
        ),
        migrations.RemoveField(
            model_name='rpv7',
            name='name',
        ),
        migrations.AlterField(
            model_name='rpv5',
            name='critical_level',
            field=models.FloatField(default=1.09, verbose_name='Критическое значение'),
        ),
        migrations.AlterField(
            model_name='rpv6',
            name='critical_level',
            field=models.FloatField(default=1.09, verbose_name='Критическое значение'),
        ),
        migrations.AlterField(
            model_name='rpv7',
            name='critical_level',
            field=models.FloatField(default=1.39, verbose_name='Критическое значение'),
        ),
    ]
