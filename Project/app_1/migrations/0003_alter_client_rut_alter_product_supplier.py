# Generated by Django 4.0.4 on 2022-05-31 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0002_supplier_working_since'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='rut',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='supplier',
            field=models.CharField(choices=[('Buenimar S.A.', 'Buenimar S.A.')], max_length=40),
        ),
    ]