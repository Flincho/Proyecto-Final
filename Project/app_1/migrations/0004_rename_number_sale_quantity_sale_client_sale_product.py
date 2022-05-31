# Generated by Django 4.0.4 on 2022-05-31 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0003_alter_client_rut_alter_product_supplier'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='number',
            new_name='quantity',
        ),
        migrations.AddField(
            model_name='sale',
            name='client',
            field=models.CharField(choices=[('Alex', 'Alex')], default='.', max_length=40),
        ),
        migrations.AddField(
            model_name='sale',
            name='product',
            field=models.CharField(choices=[('Hot Dog', 'Hot Dog'), ('French Fries', 'French Fries')], default='.', max_length=40),
        ),
    ]