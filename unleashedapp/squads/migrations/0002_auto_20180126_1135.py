# Generated by Django 2.0 on 2018-01-26 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('squads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employees.Employee'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='squad',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='squads.Squad'),
        ),
        migrations.AlterField(
            model_name='squad',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
