from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)         
    roll = models.IntegerField(unique=True)         
    email = models.EmailField(unique=True)         
    address = models.TextField()                    
    created_at = models.DateTimeField(auto_now_add=True)  # auto, ignored


    def __str__(self):
        return f"{self.name} ({self.roll})"
