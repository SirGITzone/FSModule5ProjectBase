# Generated by Django 2.2.6 on 2020-01-05 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='copy_count',
        ),
        migrations.RemoveField(
            model_name='book',
            name='price',
        ),
    ]
