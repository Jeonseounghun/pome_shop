# Generated by Django 3.1.4 on 2021-01-17 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_auto_20210116_2141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-order_date',)},
        ),
        migrations.AddField(
            model_name='product',
            name='price_text',
            field=models.TextField(default=''),
        ),
    ]
