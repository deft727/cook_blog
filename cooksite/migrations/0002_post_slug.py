# Generated by Django 3.2.2 on 2021-05-10 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooksite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', max_length=200),
        ),
    ]
