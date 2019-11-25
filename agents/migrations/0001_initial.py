# Generated by Django 2.2.7 on 2019-11-18 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('B', 'Buying Agent'), ('S', 'Selling Agent'), ('R', 'Real Estate Brooker')], max_length=50)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='photos')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Agents',
            },
        ),
    ]
