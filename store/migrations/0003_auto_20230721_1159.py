# Generated by Django 3.2.17 on 2023-07-21 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20230720_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='uploads/products/'),
        ),
    ]