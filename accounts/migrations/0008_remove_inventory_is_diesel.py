# Generated by Django 3.1 on 2020-09-02 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_employee_car_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='is_diesel',
        ),
    ]