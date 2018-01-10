# Generated by Django 2.0 on 2017-12-22 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('habitats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('function', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('visible_site', models.BooleanField()),
                ('habitat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habitats.Habitat')),
            ],
        ),
    ]
