# Generated by Django 2.0 on 2018-01-26 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('floorplan', '0002_auto_20180126_1135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='space',
            old_name='employee_id',
            new_name='employee',
        ),
    ]
