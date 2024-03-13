from django.db import models

# Create your models here.
class Plant(models.Model):
    common_names = models.CharField(max_length=100)
    botanical_name = models.CharField(max_length=100)
    light_need = models.TextField(max_length=500)
    water_need = models.TextField(max_length=500)
    soil_type = models.TextField(max_length=500)
    leaf_description = models.TextField(max_length=500)
    toxic = models.BooleanField(default=True)
    native_to = models.TextField(max_length=250)
    acquired_via = models.TextField(max_length=250) 


    def __str__(self):
        return f'{self.common_names} ({self.id})'
    