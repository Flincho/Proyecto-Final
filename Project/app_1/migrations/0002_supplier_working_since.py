# Generated by Django 4.0.4 on 2022-05-29 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='working_since',
            field=models.DateField(default='2000-01-01'),
        ),
    ]