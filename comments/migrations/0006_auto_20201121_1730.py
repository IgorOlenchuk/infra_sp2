# Generated by Django 3.0.5 on 2020-11-21 14:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_auto_20201119_1752'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '0005_auto_20201115_1214'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
    ]