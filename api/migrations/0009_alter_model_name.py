# Generated by Django 4.0.3 on 2022-03-28 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_delete_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='Name',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
