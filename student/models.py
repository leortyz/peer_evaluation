from django.db import models
from decouple import config
# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=200, default=config('DEFAULT_STUDENT_NAME'))
    enrollment=models.PositiveIntegerField(unique=True)
    def __str__(self):
        return str(self.enrollment)+"_"+self.name
 
