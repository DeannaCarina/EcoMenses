# Generated by Django 3.2 on 2022-04-25 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product_count',
            field=models.IntegerField(default=0),
        ),
    ]