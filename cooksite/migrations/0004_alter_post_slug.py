# Generated by Django 3.2.2 on 2021-05-29 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooksite', '0003_auto_20210511_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', max_length=200, unique=True),
        ),
    ]