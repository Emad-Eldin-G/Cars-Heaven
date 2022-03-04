# Generated by Django 4.0.3 on 2022-03-04 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('Car_ID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Brand', models.CharField(max_length=15)),
                ('Name', models.CharField(max_length=15)),
                ('Model', models.IntegerField(default=2005)),
                ('Type', models.CharField(choices=[('SUV', 'SUV'), ('Sedan', 'Sedan'), ('Hatchback', 'Hatchback'), ('Sport', 'Sport')], max_length=20)),
                ('Top_Speed', models.IntegerField()),
                ('Tank_Size', models.IntegerField()),
                ('Image', models.ImageField(upload_to='frontend\\static\\media')),
            ],
        ),
    ]