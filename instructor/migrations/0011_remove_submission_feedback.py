# Generated by Django 4.0.5 on 2022-06-07 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0010_alter_assignment_deadline_alter_assignment_post_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='feedback',
        ),
    ]