# Generated by Django 3.1 on 2021-08-15 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mikopo', '0024_auto_20210816_0218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grouploan',
            name='year',
        ),
        migrations.RemoveField(
            model_name='paygrouploan',
            name='year',
        ),
        migrations.RemoveField(
            model_name='paypersonalloan',
            name='year',
        ),
        migrations.RemoveField(
            model_name='personalloan',
            name='year',
        ),
    ]