# Generated by Django 4.0.4 on 2022-06-26 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_sale_final_price_sale_unit_price_alter_sale_client_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='date',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='client',
            field=models.CharField(default=' ', max_length=40),
        ),
        migrations.AlterField(
            model_name='sale',
            name='product',
            field=models.CharField(default=' ', max_length=40),
        ),
    ]