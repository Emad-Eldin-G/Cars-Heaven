# Generated by Django 4.0.3 on 2022-03-12 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_image_id_image_car_alter_model_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='Price',
            field=models.IntegerField(null=True),
        ),
    ]
