from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
  titulo =  models.CharField(max_length=200)
  cuerpo =  models.TextField()
  fecha  =  models.DateField(default=date.today)
  autor = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el modelo User de Django
  
  
  
