# Generated by Django 2.2.7 on 2019-11-21 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agents',
            name='type',
            field=models.CharField(choices=[('Buying Agent', 'Buying Agent'), ('Selling Agent', 'Selling Agent'), ('Real Estate Brooker', 'Real Estate Brooker')], max_length=50),
        ),
    ]
