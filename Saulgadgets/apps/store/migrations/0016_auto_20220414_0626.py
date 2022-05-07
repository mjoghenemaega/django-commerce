# Generated by Django 3.1.8 on 2022-04-14 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20201023_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='New_arrival',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='flashsale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='top_picks',
            field=models.BooleanField(default=False),
        ),
    ]