# Generated by Django 3.2.4 on 2021-06-10 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.PositiveBigIntegerField(default=0)),
                ('stock', models.PositiveBigIntegerField(default=0)),
            ],
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': (('uya_post', 'Can test pos'),)},
        ),
    ]