# Generated by Django 3.1 on 2021-07-22 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20210722_2340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='goup_id',
            new_name='group_id',
        ),
    ]
