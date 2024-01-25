from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ToDo(models.Model):
    status_choices = [
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
    ]
    priority_choices = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=15, choices=status_choices)
    date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=15, choices=priority_choices)

    def __str__(self):
        return self.title
