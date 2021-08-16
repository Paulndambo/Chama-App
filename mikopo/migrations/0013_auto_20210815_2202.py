# Generated by Django 3.1 on 2021-08-15 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mikopo', '0012_auto_20210815_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='grouploan',
            name='amount_repaid',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='grouploan',
            name='amount_to_repay',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='grouploan',
            name='balance',
            field=models.FloatField(default=0),
        ),
    ]
