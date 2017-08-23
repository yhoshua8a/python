from django.db import models

# Create your models here.

class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length = 180)
    description = models.TextField()

    #definir como se imprimiran objetos

    def __str__(self):
        return self.name
