# Generated by Django 2.0 on 2017-12-13 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='habitat',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
