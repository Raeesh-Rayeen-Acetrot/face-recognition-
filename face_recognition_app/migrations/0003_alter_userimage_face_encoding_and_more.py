# Generated by Django 5.0.1 on 2024-02-28 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face_recognition_app', '0002_alter_userimage_face_encoding_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='face_encoding',
            field=models.BinaryField(),
        ),
        migrations.AlterField(
            model_name='userimage',
            name='face_locations',
            field=models.JSONField(),
        ),
    ]
