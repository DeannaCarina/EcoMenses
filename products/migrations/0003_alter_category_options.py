# Generated by Django 3.2 on 2022-04-24 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_size_explanation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
