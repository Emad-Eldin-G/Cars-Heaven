# Generated by Django 4.0.3 on 2022-04-17 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_blog_thumbnail_alter_brand_brandimage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Body',
            field=models.FilePathField(path='blogs'),
        ),
    ]