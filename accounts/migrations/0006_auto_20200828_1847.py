# Generated by Django 3.1 on 2020-08-28 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_employee_is_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='commission',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='month_sales',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='target',
        ),
        migrations.CreateModel(
            name='employee_performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_sales', models.PositiveBigIntegerField()),
                ('target', models.PositiveBigIntegerField()),
                ('commission', models.PositiveBigIntegerField()),
                ('emp_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.employee')),
            ],
        ),
    ]