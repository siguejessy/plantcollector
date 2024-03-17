from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
('THF', 'Tropical Houseplant Food'),
('BHF', 'Blooming Houseplant Food'),
('IHF', 'Indoor Houseplant Food'),
('NF', 'New Fertilizer'),
('LS', 'Leaf Shine'),
('ATT', 'Attention')
)

class Holder(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('holder_detail', kwargs={'pk': self.id})

class Plant(models.Model):
  common_name = models.CharField(max_length=100)
  botanical_name = models.CharField(max_length=100)
  light_need = models.TextField(max_length=500)
  water_need = models.TextField(max_length=500)
  soil_type = models.TextField(max_length=500)
  description = models.TextField(max_length=500)
  native_to = models.TextField(max_length=250)
  acquired_via = models.TextField(max_length=250) 
  holders = models.ManyToManyField(Holder)
  
  def __str__(self):
    return f'{self.common_name} ({self.id})'
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'plant_id': self.id})
  
  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Feeding(models.Model):
  date = models.DateField('Feeding Date')
  meal = models.CharField(
    max_length=5,
    choices=MEALS,
    default=MEALS[0][0]
)

plant = models.ForeignKey(
    Plant,
    on_delete=models.CASCADE
)

def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"

class Meta:
    ordering = ['-date']
