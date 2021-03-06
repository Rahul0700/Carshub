# Generated by Django 3.1 on 2020-10-07 07:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20201007_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='city',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='door_no',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='pin_code',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='state',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='street',
        ),
        migrations.AddField(
            model_name='employee',
            name='city',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='employee',
            name='door_no',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='employee',
            name='pin_code',
            field=models.CharField(max_length=6, null=True, validators=[django.core.validators.MinLengthValidator(6)]),
        ),
        migrations.AddField(
            model_name='employee',
            name='state',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='employee',
            name='street',
            field=models.CharField(default='', max_length=40),
        ),
    ]
