from django.db import models

# Create your models here.
class Car(models.Model):

    type_choices = (
        ("SUV", "SUV"), 
        ("Sedan", "Sedan"), 
        ("Hatchback", "Hatchback"),
        )

    Car_ID    = models.AutoField(primary_key=True, unique=True, null=False, blank=False, )
    Brand     = models.CharField(max_length=15)
    Name      = models.CharField(max_length=15)
    Model     = models.IntegerField(default=2005)
    Type      = models.CharField(choices=type_choices, max_length=20)
    Top_Speed = models.IntegerField()
    Tank_Size = models.IntegerField()
    Image     = models.ImageField(upload_to = 'frontend\static\media')
    

    def __str__(self):
        return (f"{self.Model} {self.Brand} {self.Name}")