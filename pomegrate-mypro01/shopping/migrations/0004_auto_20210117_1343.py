# Generated by Django 3.1.4 on 2021-01-17 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_auto_20210117_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.TextField(default='', max_length=100, verbose_name='주문상품'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=99),
        ),
    ]
