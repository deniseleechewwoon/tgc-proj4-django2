# Generated by Django 3.0.6 on 2020-05-21 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_product', '0012_auto_20200521_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_posted',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]