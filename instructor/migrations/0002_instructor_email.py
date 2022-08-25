# Generated by Django 4.0.5 on 2022-06-03 11:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
    ]
