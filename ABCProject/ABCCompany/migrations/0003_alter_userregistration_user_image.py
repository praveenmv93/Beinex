# Generated by Django 3.2.8 on 2021-10-22 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ABCCompany', '0002_userregistration_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='user_image',
            field=models.ImageField(default=1, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
