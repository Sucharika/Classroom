# Generated by Django 4.0.5 on 2022-06-07 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0008_alter_assignment_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='deadline',
            field=models.CharField(max_length=256),
        ),
    ]
