# Generated by Django 3.1 on 2021-07-23 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_member_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='year',
            field=models.CharField(choices=[('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025')], default='2021', max_length=4),
        ),
    ]
