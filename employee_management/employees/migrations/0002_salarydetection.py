# Generated by Django 3.2.25 on 2024-07-04 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalaryDetection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detect_on_absent', models.IntegerField(default=0)),
                ('detect_on_late', models.IntegerField(default=0)),
            ],
        ),
    ]
