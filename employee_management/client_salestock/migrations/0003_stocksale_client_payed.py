# Generated by Django 3.2.25 on 2024-07-04 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_salestock', '0002_auto_20240704_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocksale',
            name='client_payed',
            field=models.DecimalField(decimal_places=3, default=2, max_digits=10),
            preserve_default=False,
        ),
    ]
