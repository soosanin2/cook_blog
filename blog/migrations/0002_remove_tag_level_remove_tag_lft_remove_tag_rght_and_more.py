# Generated by Django 4.2.3 on 2023-07-10 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='level',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='tree_id',
        ),
    ]