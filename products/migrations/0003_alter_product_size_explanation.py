# Generated by Django 3.2 on 2022-05-28 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_size_explanation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size_explanation',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
