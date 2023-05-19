# Generated by Django 4.2.1 on 2023-05-18 12:22

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(db_index=True, help_text='Логин пользователя', max_length=100, unique=True, verbose_name='Логин')),
                ('password', models.CharField(help_text='Пароль пользователя', max_length=255, verbose_name='Пароль')),
                ('first_name', models.CharField(help_text='Имя', max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(help_text='Фамилия', max_length=50, verbose_name='Фамилия')),
                ('email', models.EmailField(db_index=True, help_text='Email', max_length=50, unique=True, verbose_name='Email')),
                ('is_subcribed', models.BooleanField(default=False, help_text='Подписка на автора', verbose_name='Подписка на автора')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'ordering': (['username'],),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
