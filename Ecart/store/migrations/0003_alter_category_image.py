# Generated by Django 4.1.2 on 2022-11-22 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_name_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='category'),
        ),
    ]
