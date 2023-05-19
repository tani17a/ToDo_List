from django.db import models

class Task(models.Model):
    Tittle = models.CharField(max_length=30)
    Description = models.TextField()
    Time=models.TimeField(auto_now=True)

    def __str__(self):
        return self.Tittle
    