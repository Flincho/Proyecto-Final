# Generated by Django 4.0.4 on 2022-06-22 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('rut', models.IntegerField()),
                ('address', models.CharField(max_length=40)),
            ],
        ),
    ]
