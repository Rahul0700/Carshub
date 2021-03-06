# Generated by Django 3.1 on 2020-10-07 07:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20201007_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='customer',
            name='door_no',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='customer',
            name='pin_code',
            field=models.CharField(max_length=6, null=True, validators=[django.core.validators.MinLengthValidator(6)]),
        ),
        migrations.AddField(
            model_name='customer',
            name='state',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='customer',
            name='street',
            field=models.CharField(default='', max_length=40),
        ),
    ]
