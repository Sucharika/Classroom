# Generated by Django 4.0.5 on 2022-06-07 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0007_alter_assignment_deadline_alter_assignment_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='deadline',
            field=models.DateField(max_length=100),
        ),
    ]
