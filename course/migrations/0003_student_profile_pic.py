# Generated by Django 4.0.5 on 2022-06-04 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_remove_student_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile/'),
        ),
    ]
