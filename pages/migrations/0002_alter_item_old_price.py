# Generated by Django 4.0.6 on 2022-07-18 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='old_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
