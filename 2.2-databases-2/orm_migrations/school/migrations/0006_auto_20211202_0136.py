# Generated by Django 3.2.9 on 2021-12-01 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_teacher_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='teacher',
            new_name='teachers',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='student',
        ),
    ]
