# Generated by Django 4.2.7 on 2024-03-01 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0002_alter_client_model_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client_model',
            old_name='updated_by',
            new_name='updated_at',
        ),
    ]
