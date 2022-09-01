from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=25)
    roll=models.CharField(max_length=25)
    college=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
    email=models.EmailField()
    def __str__(self):
        return '{0.name}{0.roll}{0.college}{0.password}{0.email}'.format(self)