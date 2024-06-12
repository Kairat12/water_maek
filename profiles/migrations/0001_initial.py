# Generated by Django 4.2.13 on 2024-06-11 09:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('givenName', models.CharField(blank=True, help_text='Введите имя', max_length=100)),
                ('lastName', models.CharField(blank=True, max_length=100)),
                ('patronymicName', models.CharField(blank=True, help_text='Введите отчество', max_length=100)),
                ('timesheet_number', models.CharField(blank=True, max_length=5, null=True)),
                ('company', models.CharField(blank=True, max_length=500)),
                ('department', models.CharField(blank=True, max_length=500)),
                ('position', models.CharField(blank=True, max_length=500)),
                ('mail', models.EmailField(blank=True, max_length=100)),
                ('is_worker', models.BooleanField(default=True, verbose_name='Статус сотрудника')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data created')),
                ('update_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Date updated')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль пользователя',
                'verbose_name_plural': 'Профиль пользователей',
            },
        ),
    ]
