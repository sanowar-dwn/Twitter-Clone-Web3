# Generated by Django 4.2.1 on 2023-09-01 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0004_devicelog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devicelog',
            name='condition_at_checkout',
        ),
        migrations.RemoveField(
            model_name='devicelog',
            name='device',
        ),
        migrations.RemoveField(
            model_name='devicelog',
            name='employee',
        ),
        migrations.AddField(
            model_name='devicelog',
            name='device_assignment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='device.deviceassignment'),
            preserve_default=False,
        ),
    ]