# Generated by Django 4.2.3 on 2023-08-02 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_app', '0002_alter_post_admin_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='admin_post',
            new_name='user',
        ),
    ]
