# Generated by Django 3.1 on 2021-07-22 20:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='date_formed',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
