# Generated by Django 4.2.7 on 2024-03-02 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projectapp', '0002_remove_project_model_users_project_model_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_model',
            name='users',
        ),
        migrations.AddField(
            model_name='project_model',
            name='users',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_users', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
