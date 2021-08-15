# Generated by Django 3.1 on 2021-08-15 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoanType',
            fields=[
                ('title', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('period', models.FloatField(default=0)),
                ('interest_rate', models.FloatField(default=0)),
            ],
        ),
    ]