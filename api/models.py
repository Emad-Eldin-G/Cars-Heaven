from importlib.resources import path
from pyexpat import model
from django.db import models

# Create your models here.
class Brand(models.Model):
    Name        = models.CharField(primary_key=True, unique=True, null=False, blank=False, max_length=25)
    BrandImage  = models.ImageField(upload_to = 'frontend\static\media')
    
    def __str__(self):
        return (f"{self.Name}")

class Model(models.Model):
    types = (
        ("SUV", "SUV"), 
        ("Sedan", "Sedan"), 
        ("Hatchback", "Hatchback"),
        ("Sport", "Sport"),
        )


    power = (
        ("Gas", "Gas"), 
        ("Electric", "Electric"), 
        ("Hybrid", "Hybrid"),
        ("Hydrogen", "Hydrogen"),
        )
        
    years = (
    (2015, '2015'),
    (2016, '2016'),
    (2017, '2017'),
    (2018, '2018'),
    (2019, '2019'),
    (2020, '2020'),
    (2021, '2021'),
    (2022, '2022'),
    (2023, '2023'),
    (2024, '2024'))

    Name         = models.CharField(max_length=25, null=True)
    Year         = models.IntegerField(choices=years) 
    Brand        = models.ForeignKey('Brand', null=True, on_delete=models.CASCADE)
    Type         = models.CharField(choices=types, max_length=20, default='Sedan')
    Power        = models.CharField(choices=power, default='Gas', max_length=12)
    Price        = models.PositiveIntegerField(null=True) #MSRP
    Top_Speed    = models.PositiveIntegerField(null=True) #In miles
    Milage       = models.PositiveIntegerField(null=True)
    Tank_Size    = models.PositiveIntegerField(null=True, blank=True) #Null if electric=True
    Images       = models.ForeignKey('Image', on_delete=models.PROTECT, null=True, blank=True)
    
    def __str__(self):
        return (f"{self.Name}")

class Image(models.Model):
    Car            = models.ForeignKey('Model', primary_key=True, on_delete=models.CASCADE)
    Front          = models.ImageField(upload_to = 'frontend\static\media')
    Back           = models.ImageField(upload_to = 'frontend\static\media')
    Side           = models.ImageField(upload_to = 'frontend\static\media')
    Interior_Front = models.ImageField(upload_to = 'frontend\static\media')
    Interior_Back  = models.ImageField(upload_to = 'frontend\static\media')
    On_Road        = models.ImageField(upload_to = 'frontend\static\media')
    
    def __str__(self):
        return (f"{self.Car}")

class Blog(models.Model):
    Car        = models.ForeignKey('Model', on_delete=models.PROTECT, null=True, blank=True)
    Title      = models.CharField(null=True, max_length=50)
    Created_at = models.DateField(auto_now_add=True)
    Body       = models.FilePathField(path='blogs', recursive=True)

    def __str__(self):
        return (f"{self.Title}")