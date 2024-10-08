# Generated by Django 3.2.25 on 2024-08-02 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20240802_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='jacket',
            name='code',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shirt',
            name='brand_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shirt',
            name='code',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='t_shirt',
            name='brand_name',
            field=models.CharField(default=12, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='t_shirt',
            name='code',
            field=models.CharField(default=123, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pant',
            name='brand_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='shorts',
            name='brand_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='trouser',
            name='brand_name',
            field=models.CharField(max_length=50),
        ),
    ]
