# Generated by Django 3.2.4 on 2021-06-10 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
