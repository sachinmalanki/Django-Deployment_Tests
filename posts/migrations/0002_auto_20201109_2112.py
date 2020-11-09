# Generated by Django 3.1.2 on 2020-11-09 15:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='groups',
            new_name='group',
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together={('user', 'message', 'created_at')},
        ),
    ]