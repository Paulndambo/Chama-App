# Generated by Django 3.1 on 2021-07-23 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_auto_20210723_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='grouptotalsaving',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
