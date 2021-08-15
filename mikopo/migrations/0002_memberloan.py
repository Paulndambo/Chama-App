# Generated by Django 3.1 on 2021-08-15 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_group_year'),
        ('mikopo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberLoan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.member')),
            ],
        ),
    ]
