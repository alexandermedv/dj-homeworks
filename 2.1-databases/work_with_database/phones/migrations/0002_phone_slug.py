# Generated by Django 3.2.9 on 2021-11-27 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='slug',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
    ]
