# Generated by Django 3.1 on 2021-08-15 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mikopo', '0025_auto_20210816_0227'),
    ]

    operations = [
        migrations.AddField(
            model_name='grouploan',
            name='year',
            field=models.IntegerField(default=2021),
        ),
        migrations.AddField(
            model_name='paygrouploan',
            name='year',
            field=models.IntegerField(default=2021),
        ),
        migrations.AddField(
            model_name='paypersonalloan',
            name='year',
            field=models.IntegerField(default=2021),
        ),
        migrations.AddField(
            model_name='personalloan',
            name='year',
            field=models.IntegerField(default=2021),
        ),
    ]
