# Generated by Django 3.2.9 on 2022-01-07 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20220107_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='scopes', through='articles.Scope', to='articles.Tag'),
        ),
    ]