# Generated by Django 4.0.3 on 2022-03-02 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_car_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='Image',
            field=models.ImageField(default=1, upload_to='frontend\\static\\media'),
            preserve_default=False,
        ),
    ]
