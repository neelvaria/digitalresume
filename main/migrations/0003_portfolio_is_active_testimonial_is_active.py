# Generated by Django 4.2.7 on 2023-11-22 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_image_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
